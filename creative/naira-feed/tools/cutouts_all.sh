#!/bin/bash
# one process per piece so BiRefNet's memory is returned between pieces
cd /tmp/claude-0/-home-user/aceb438e-f1c8-5500-8bc9-95c87202d43a/scratchpad/feed
for h in $(echo "$1" | tr ',' ' '); do OMP_NUM_THREADS=3 python3 tools/cutouts.py "$h"; done
