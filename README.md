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

## Hasil trial practice

Diukur lokal vs env kit, 6 game/trial, 100.000 node/langkah:

| trial | Elo | menang | seri | kalah |
|-------|-----|--------|------|--------|
| trial-0 | 1545 | 4 | 1 | 1 |
| trial-1 | 1364 | 3 | 1 | 2 |
| trial-2 | 1279 | 3 | 0 | 3 |
| **rata-rata** | **1396** | | | |

Rata-rata 1396 di atas floor final 1.154 dan baseline sunfish ~1.325.
Deterministic: trial yang sama diulang memainkan langkah yang sama —
trial-0 versi packed dan unpacked identik (1545, 4W 1D 1L).

## Cara kerja engine

Sekali jalan, engine ini berputar dalam satu loop sederhana: minta posisi
dari env, cari langkah terbaik, kirim langkah itu, lalu terapkan balasan
lawan dan ulangi sampai permainan selesai.

Papan disimpan sebagai array 0x88 — 128 kotak, 64 di antaranya valid —
sehingga pengecekan "kotak ini di luar papan?" cukup satu operasi bit.
Setiap langkah dikodekan dalam satu integer 16 bit: kotak asal, kotak
tujuan, dan bidak promosi. Generator langkah menangani semua aturan
catur: rokade, en passant, dan promosi ke empat bidak.

Pencarian memakai alpha-beta dengan pendalaman iteratif: mulai dari
kedalaman 1, naik satu tingkat demi satu tingkat, sampai anggaran node
habis. Anggarannya tetap — 100.000 node per langkah — jadi tidak ada jam
yang dibaca dan tidak ada angka acak; posisi yang sama selalu menghasilkan
langkah yang sama. Quiescence search menenangkan posisi yang masih
"panas" (ada tangkapan, promosi, atau balasan cek yang menggantung)
sebelum evaluasi dibaca. Tabel transposisi (kunci Zobrist, seed tetap)
menyimpan hasil pencarian supaya posisi yang berulang tidak dihitung dua
kali, dan urutan langkah (tangkapan besar dulu, langkah dari tabel dulu)
membuat pemotongan alpha-beta bekerja lebih awal.

Evaluasi posisinya ringan: nilai material tiap bidak ditambah bonus
posisi dari tabel piece-square setengah lebar (simetris kiri-kanan),
plus bonus kecil kalau punya sepasang gajah. Tidak ada jaringan saraf,
tidak ada buku bukaan — semua keputusan lahir dari pencarian di atas
papan saat itu juga.

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
