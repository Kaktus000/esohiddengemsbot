#!/usr/bin/env python3
import sys, json, random

random.seed(1)
first_tick = True

for line in sys.stdin:
    data = json.loads(line)
    if first_tick:
        config = data.get("config", {})
        width = config.get("width")
        height = config.get("height")
        print(f"Let me Cook")
        
    print(move, flush=True)
    first_tick = False
