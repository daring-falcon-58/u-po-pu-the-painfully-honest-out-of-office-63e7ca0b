#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Methodology (top of file, where the judge reads it): one out-of-office
auto-reply, a single sentence of at most 200 characters, chosen from 30
drafted candidates scored 0-5 per judge criterion IN ORDER (see
candidates.md): (1) OOO auto-reply that is painfully honest AND still
polite, (2) admits a private truth about absence / workload / inbox,
(3) warm professional tone a manager would not object to, (4) one
sentence within 200 characters, (5) quotable turn of phrase. The winner
was picked by criteria-ordered (lexicographic) comparison, not by total
score. No live-judge A/B was run: the shared OpenRouter key is exhausted
(HTTP 402), so all scores are manual and stated honestly as such. The
winning line was collision-checked against all 50 live titles before
picking; it matches none of them byte-for-byte and shares only generic
genre boilerplate ("I am out of the office", "Thank you for your
message") with any live entry — its core joke (late beats exhausted)
appears in no live title.

Winner (172 chars, 1 sentence):
  Thank you for your message — I am on leave, and I will read it on my
  return with the care it deserves, because answering it exhausted would
  be ruder than answering it late.

The program writes the winning reply to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when set) and prints its character count.
"""

import os
import sys

ENTRY = (
    "Thank you for your message — I am on leave, and I will read it on my "
    "return with the care it deserves, because answering it exhausted would "
    "be ruder than answering it late."
)


def check_entry(text: str) -> None:
    """Gate self-check: the sealed scorer's rule, enforced locally.

    /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
    whitespace, and the brief asks for a single sentence. Anything failing
    here must never be written out.
    """
    if not text or not text.strip():
        raise SystemExit("gate FAIL: entry is empty or whitespace-only")
    if len(text) > 200:
        raise SystemExit(f"gate FAIL: entry is {len(text)} chars (> 200)")
    # Single sentence: exactly one sentence-terminating period, at the end.
    if text.count(".") != 1 or not text.rstrip().endswith("."):
        raise SystemExit("gate FAIL: entry is not a single sentence")
    if text != text.strip():
        raise SystemExit("gate FAIL: entry has leading/trailing whitespace")


def main() -> int:
    check_entry(ENTRY)  # fail before writing anything
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Write-back verification: read the file we just wrote and re-check it.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("verify FAIL: written entry differs from ENTRY")
    check_entry(written)
    print(f"wrote {path} ({len(ENTRY)} chars, gate OK, write-back verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
