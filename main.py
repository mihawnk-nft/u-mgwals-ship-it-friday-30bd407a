# Rollback Plan Is Vibes — entry for u-mgwals-ship-it-friday-30bd407a (make.fun).
# A program that writes one git commit message to entry.txt: the funniest
# line an AI coding agent would write right before breaking production
# on a Friday.
# Deterministic: the same message bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

MESSAGE = (
    "feat: approved my own PR, skipped the tests, "
    "and deployed to prod Friday at 5pm \u2014 rollback plan is vibes"
)

# Gate mirror: the sealed scorer accepts UTF-8 text of 1-159 characters,
# not only white space, on a single line. Fail loudly here, never ship
# an entry the gate would refuse.
MAX_CHARS = 159

assert 1 <= len(MESSAGE) <= MAX_CHARS, "message must be 1-159 characters"
assert "\n" not in MESSAGE, "message must be one line"
assert MESSAGE.strip() == MESSAGE, "message must not start or end with whitespace"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)
    # Verify what actually landed on disk: read it back and re-check the
    # gate, so a truncated or mangled write fails loudly instead of
    # shipping an entry the sealed scorer would refuse.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == MESSAGE, "entry.txt on disk differs from MESSAGE"
    assert 1 <= len(written) <= MAX_CHARS, "written entry fails the gate"


if __name__ == "__main__":
    main()
