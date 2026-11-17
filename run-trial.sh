#!/bin/bash
# Run one local practice trial: start env, run engine, score it.
# usage: run-trial.sh <trial-n> <engine-dir> [tag]
set -u
KIT=~/workspace/makefun/tiny-chess-01-kit/tiny-chess-01-kit
TRIAL=${1:-0}
ENG=${2:-~/workspace/makefun/tiny-chess}
TAG=${3:-t$TRIAL}
STATE=/tmp/tc-state-$TAG
SCORES=/tmp/tc-scores-$TAG
rm -rf "$STATE" "$SCORES"; mkdir -p "$STATE" "$SCORES"
MAKEFUN_ENV_DATA_DIR="$KIT/practice/trial-$TRIAL/input/env" \
MAKEFUN_STATE_DIR="$STATE" MAKEFUN_ENV_PORT=8123 \
node "$KIT/program/env/server.mjs" >/tmp/tc-env-$TAG.log 2>&1 &
ENVPID=$!
for i in $(seq 1 50); do [ -f "$STATE/ready" ] && break; sleep 0.1; done
[ -f "$STATE/ready" ] || { echo "env did not start"; cat /tmp/tc-env-$TAG.log; kill $ENVPID 2>/dev/null; exit 1; }
T0=$(python3 -c 'import time;print(time.time())')
(cd "$ENG" && MAKEFUN_ENV_URL=http://127.0.0.1:8123 timeout 1750 python3 main.py 2>/tmp/tc-eng-$TAG.log)
EC=$?
T1=$(python3 -c 'import time;print(time.time())')
kill -TERM $ENVPID 2>/dev/null; sleep 0.5; kill -9 $ENVPID 2>/dev/null
echo "engine exit=$EC wall=$(python3 -c "print(f'{$T1-$T0:.0f}s')")"
tail -8 /tmp/tc-eng-$TAG.log
[ -f "$STATE/export/state.json" ] || { echo "NO state.json exported"; exit 1; }
MAKEFUN_OUTPUT_DIR="$STATE/export" MAKEFUN_REFERENCE_DIR="$KIT/practice/trial-$TRIAL/reference" \
MAKEFUN_SCORES_DIR="$SCORES" node "$KIT/program/scorer/score.mjs"
cat "$SCORES/scores.json"
