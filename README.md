# tiny-chess

[![competition](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Harianrevi1/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Harianrevi1/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01)

A chess engine in 4 KB of Python, built for the
[make.fun bounty "Build the strongest chess engine in 4 KB of Python"](https://make.fun/bounty/tiny-chess-01).

`main.py` is the whole engine (packed with `lzma` + base85; the payload and
the unpacker fit in 4,096 bytes). It plays the house gauntlet through the
env at `MAKEFUN_ENV_URL` (`POST /game`, `POST /move`) and searches with:

- 0x88 board, full move generation (castling, en passant, promotions)
- alpha-beta with iterative deepening to a fixed node budget (deterministic,
  no clock, no randomness) — 100,000 nodes a move
- quiescence search (captures, promotions, replies to checks)
- transposition table, MVV-LVA move ordering, late-move reductions,
  null-move pruning
- evaluation: material + piece-square tables + bishop pair

Practice Elo (local, vs the kit's env): trial-0 1451, trial-1 1279,
trial-2 1099 at 100,000 nodes (mean ~1276, above the 1,154 final floor).
Deterministic: the same trial replayed plays the same moves.

## The size rule

- `main.py` is the whole engine: at most 4,096 bytes as committed,
  Python 3.13, standard library only. It reads, imports or execs no other
  file in the repository.
- Compression is allowed and counted. A `main.py` that unpacks and execs
  a compressed payload (`lzma`, `zlib`) is fine; the payload and the
  unpacker are both part of its 4,096 bytes.
- The rest of the tree (this README, LICENSE) is at most 8,192 bytes in
  all, and no file over 4,096.

## License

MIT, see LICENSE.
