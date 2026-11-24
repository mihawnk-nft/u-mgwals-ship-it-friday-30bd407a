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
assert 1 <= len(MESSAGE) <= 159, "message must be 1-159 characters"
assert "\n" not in MESSAGE, "message must be one line"
assert MESSAGE.strip() == MESSAGE, "message must not start or end with whitespace"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
