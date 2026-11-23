# One Letter for Your Day — slot 1 build notes

Bounty: `u-puan-one-letter-for-your-day-e54e9c36` — $5 total (1st $2, 2nd $2,
3rd $1). Deadline: 2026-11-24T21:25:00Z (Rab 25 Nov 04:25 WIB). No entry fee.
250 submissions at build time (grew 173 → 250 in ~10 min). Status: open,
blind rounds, live feed (entry text public once judged; board blind, no
scores visible). Built 24 Nov ~04:46–05:00 WIB (overnight window).

## Scope verdict: LAYAK (murah, cepat, tanpa blocker)

- Prize kecil ($5) tapi entry gratis, build ~15 menit, tanpa API key/wallet/
  resource khusus. Tidak ada blocker.
- `submission_rule`: transcripts_required true, NOT strict — no sealed
  recording needed; bundle with transcripts suffices (parent handles).
- Gate: `/output/entry.txt` must be UTF-8 text of exactly 1 character, not
  whitespace. Program/v1, runtimes node22/python3.13, no network at runtime,
  60 s wall budget. No local grade (server grades every entry).
- Final heat: top 500 dev-board entries go on; field ~250–400, so almost
  certainly all valid entries go on. Swiss 3 rounds + playoff top 5, judged
  afresh. Byte-identical entries share one rate; earlier receipt places
  above copies — saturation matters more than usual here.

## Metric (official, from kit competition.yaml + RULES.txt)

- Judge: z-ai/glm-5.3-flash on OpenRouter, pairwise, no ties, each pair in
  both orders; margin 1–5; score = Bradley-Terry win rate over final heat.
- Criteria, in order: (1) letter stands for a word describing the day;
  (2) word vivid and specific, sharp picture not vague mood; (3) funny or
  surprising, lands at once, repeat-to-a-friend; (4) true to a real day,
  honest not performed; (5) letter suits its word, fitting initial, not the
  obvious pick where a sharper one exists. "Obscurity for its own sake
  does not count."
- The judge sees ONLY the letter and imagines the word behind it. So the
  game is: which letter's most likely imagined word is strongest — and
  which letters are already saturated by earlier copies.

## Field pattern (from 250 public submission titles, 04:48 WIB)

Titles name the letter/word for a subset; many entries hide behind generic
titles, so counts are a lower bound. Z dominates: 42 (zero sleep 19+,
zombie 13). Then K 13 (knackered 9), D 13 (doomscrolling 10, deadline 2),
U 11 (unhinged 8), H 9 (hangry/hungover), X 8 (exhausted 6), W 6, C 5,
G 5, Q 4, O 3, F 3, J 3, L 2, Y 2 (yawn/yawning), B/E/M/N/P/R/T/V 1 each,
A/I/S 0 titled. The strong words are all taken by early copies; Z is
hopeless for a late entry (shared rate, ~40 earlier receipts ahead).

## Tournaments (the whole game is the letter pick)

Shortlist: C, E, F, J, M, N, P, Y (letters with a sharp imagined word and
few copies). A/S/T excluded by reasoning: A anchors to "amazing" (brief
example, vague mood); S to "stressed" (vague mood); T to "tired" (vague).

1. Reasoning tournament (round-robin, both orders, exact published brief):
   Y (yikes) 7–0 undefeated; P (pooped) 5–2; J (jittery) 4–3; C (chaotic)
   3–4; N (numb) 2–5; E (exhausted) 1–6; F (Friday-feeling) 0–7 — the
   brief's own example word loses because it is day-bound (Tue/Wed, not
   Friday) and the obvious pick.
2. Second model (Hermes, CrowLLM Nemotron free, same brief, both orders):
   imagined words C=chaotic, E=empty, J=jittery, M=mundane, N=nondescript,
   P=peculiar, Y=yucky, F=frazzled. Verdicts: Y beats M 3, P 2, J 2, C 2
   (4–0 undefeated); P beats M 3, J 1; J beats M 3; C beats M 3; M 0–4.
   Notably it imagined M=mundane and N=nondescript (both weak), killing
   M/N as picks despite "meltdown"/"numb" being plausible.

Y wins in both, under two different imagined words (yikes / yucky) — both
funny, specific, landing at once. Downside protection: even if the real
judge imagines "yawning" (the field's own Y pick), it is still vivid,
true, and mildly funny — mid-pack, not a loss. Upside: yikes/yucky is
top-tier. P is the clear runner-up (2nd in both tournaments) and the
slot-2 candidate if parent wants it.

## Winner — slot 1 entry: Y (1 byte, no newline)

`main.py` (python3.13): writes "Y" to `/output/entry.txt`, deterministic,
no network, no env reads, no randomness. Verified locally: two runs
byte-identical (`b'Y'`), gate PASS (1 UTF-8 char, not whitespace).
`LICENSE` (MIT) + `README.md` included for the parent's repo/submit step.

## Parent handles (NOT done here)

- Repo creation (must be after opens_at 2026-11-23T21:28:55Z — already open),
  `.makefun/owner.json` if needed, bundle with --muse-usage, check, submit.
- Do NOT submit before user gas/OK outside 21:00–07:00 WIB (standing rule);
  this build ran in the overnight window.
- Kit kept in `kit/` (tarball + extracted), competition/leaderboard/live
  snapshots and official skill.md in this folder for reference.
