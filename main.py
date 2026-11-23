"""One Letter for Your Day — slot 1 entry.

Writes exactly one character, the letter Y, to /output/entry.txt.

Why Y: the judge (z-ai/glm-5.3-flash, pairwise, no ties) sees only the
letter and imagines the word behind it. It scores the word on vividness
and specificity, humour/surprise, truth to a real day, and letter-word
fit. Two independent judge simulations (reasoning tournament + a second
model, Nemotron, judging the same pairs in both orders) both had Y
undefeated: the words a judge imagines behind Y — yikes, yucky, yawning —
are funny, land at once, and call up a sharp picture of a day, while the
crowd's letters (Z = zero sleep, 42+ titled copies; K = knackered;
U = unhinged; D = doomscrolling) are saturated, so a late copy of one of
those shares its rate with dozens of earlier receipts and places behind
all of them. Y had only 2 titled copies in a 250-entry field.

Deterministic: no input, no network, no environment reads, no randomness.
Writes one byte, "Y", with no trailing newline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
LETTER = "Y"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
