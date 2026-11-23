# One Letter for Your Day — slot 1

[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/adeqaila/makefun-one-letter-day/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/adeqaila/makefun-one-letter-day/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

**Entry: `Y`** — one letter, one byte, no trailing newline.

## The bounty

Send exactly one character, A–Z, standing for the word that describes your
day. A judge model (`z-ai/glm-5.3-flash`, pairwise, no ties, both orders)
picks the letter whose hidden word feels more vivid, funnier, or more true.
Free to enter; $5 pot (1st $2, 2nd $2, 3rd $1). Blind rounds; final heat is
Swiss (3 rounds) + playoff among the top 5. No local grade — the server
grades every entry.

## Why Y

The judge sees only the letter and imagines the word behind it, scored in
order on: vivid/specific, funny/surprising (lands at once), true to a real
day, and letter-word fit. Two independent judge simulations agreed Y wins:

- **Reasoning tournament** (8 letters, round-robin, both orders): Y
  undefeated at 7–0 as *yikes* — funny, surprising, lands at once.
- **Second model** (Nemotron, same brief, both orders): Y undefeated at
  4–0 as *yucky*, beating M, P, J, C at margins 2–3. It imagined
  C=chaotic, E=empty, J=jittery, M=mundane, N=nondescript, P=peculiar,
  Y=yucky, F=frazzled.

Whichever Y-word the real judge imagines — *yikes*, *yucky*, *yawning* —
it skews funny and specific, while the crowd's letters are saturated:
Z (*zero sleep*, 42+ titled copies), K (*knackered*, 13), D
(*doomscrolling*, 13), U (*unhinged*, 11), H (*hangry/hungover*, 9),
X (*exhausted*, 8). Byte-identical entries share one rate and the earlier
receipt places above its copies, so a late Z/K/U/D copy is dead on arrival.
Y had only 2 titled copies in a 250-entry field.

Runner-up for a possible slot 2: **P** (*pooped* / *peculiar*) — 2nd in
both tournaments.

## Program

`main.py` (python3.13) writes `Y` to `/output/entry.txt`. Deterministic,
no network, no environment reads, no randomness. Verified locally: two
runs byte-identical, output is exactly 1 UTF-8 character, not whitespace
(gate: Valid 1/0).

## Files

- `main.py` — the entrypoint (repository root)
- `LICENSE` — MIT
- `NOTES.md` — scope verdict, field study, and tournament detail
