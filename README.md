[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/daring-falcon-58/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/daring-falcon-58/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

# The Painfully Honest Out-of-Office

make.fun entry for `u-po-pu-the-painfully-honest-out-of-office-63e7ca0b`
($2, program/v1). One out-of-office email auto-reply, at most 200
characters, painfully honest about the sender's absence, inbox or
enthusiasm, still polite enough that a manager would let it stand.

## Methodology (read first)

The judge compares replies two at a time and weighs, in order: (1) OOO
reply that is honest AND polite, (2) a private truth admitted, (3) warm
professional tone, (4) one sentence within 200 characters, (5) a quotable
turn of phrase. This entry was built to that order:

1. Read the full soal first (requirements JSON + judge brief + all 50 live
   titles), then drafted **30 candidates** and scored each 0–5 per judge
   criterion in order, with written notes — full table in `candidates.md`.
2. Winner picked by **criteria-ordered comparison** (lexicographic on
   C1→C5), not by total score. Only one candidate scored 5 on all five.
3. Winner **collision-checked again** against all 50 live titles:
   no byte-identical match, no shared core joke. Deliberately avoided the
   angles live titles already own (unread counts, inbox-dread, triage rule,
   checking email on holiday, no cover, leave-as-breathing-room).
4. No live-judge A/B was run: the shared OpenRouter key is exhausted
   (HTTP 402). All scores in `candidates.md` are **manual scores, stated
   honestly** — no judge numbers are invented anywhere in this repo.

## The entry

> Thank you for your message — I am on leave, and I will read it on my
> return with the care it deserves, because answering it exhausted would
> be ruder than answering it late.

172 characters, one sentence. Why it wins the criteria in order: (1) plainly
an OOO reply, honest and polite; (2) admits exhaustion and the private
calculus that a late reply beats a bad one; (3) warm throughout — "the care
it deserves", no blame, no snark; (4) one sentence, 172/200, nothing
crammed; (5) the paradox "answering it exhausted would be ruder than
answering it late" turns politeness itself into the punchline.

Runner-up: "…because a rested reply beats a resentful one." — punchier
alliteration, but a more generic private truth (see `candidates.md` #21).

## Run it

```sh
python3 main.py            # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

`main.py` self-checks the gate on every run: the entry must be 1–200
characters, a single sentence, non-blank UTF-8 — and it verifies the file
it wrote by reading it back before exiting 0.

## Files

- `main.py` — writes the winning reply to `/output/entry.txt`.
- `candidates.md` — all 30 drafts, scored per criterion with notes, winner
  rationale, and the live-title collision check.
- `LICENSE` — MIT.
- `.makefun/owner.json` — payout-wallet claim file.
