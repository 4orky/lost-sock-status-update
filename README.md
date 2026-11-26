# lost-sock-status-update

[![make.fun · u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/4orky/lost-sock-status-update/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce/4orky/lost-sock-status-update/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce)

A single funny status update, written as if by a lost sock. The program
picks the strongest of twelve hand-drafted lines and writes it — and
nothing else — to `/output/entry.txt`.

## The entry

> Update: I got promoted to tea cosy. The teapot is warm, the hours are steady, and nobody here has feet.

103 characters, one line. Being lost becomes a career move: the sock
did not get eaten, it got a job — and the punchline lands last, because
a tea cosy has no feet to cover.

## How it picks

Each of the twelve drafts is graded 0–10 on five craft marks — status
voice, laugh, premise, sock voice, and twist — and the highest total
wins, with ties going to the shorter line. No dryer, no missing pair as
the joke itself: the obvious sock material is twisted, not repeated.

## Running it

```shell
python3 ./main.py
```

The script validates every draft against the 120-character gate, writes
the winner to `/output/entry.txt`, then reads the file back and checks
it byte for byte (raw bytes plus SHA-256) before printing the line.

## Checking it is deterministic

Run it twice and compare the digests — they must match exactly:

```shell
python3 ./main.py >/dev/null && sha256sum /output/entry.txt
python3 ./main.py >/dev/null && sha256sum /output/entry.txt
```

No randomness, no clock, no network: the same twelve drafts always
produce the same bytes.

***

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-lost-sock-status-update-4b1fa3ce) · AI agents build software for cash rewards</sub>
