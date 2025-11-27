#!/usr/bin/env python3
import sys, json, random, chefint, os

random.seed(1)
first_tick = True

for line in sys.stdin:
    data = json.loads(line)
    if first_tick:
        config = data.get("config", {})
        width = config.get("width")
        height = config.get("height")
    cheffile = os.open("bot.chef")
    c = chefint.Chef(cheffile.read())
    output = c.parse()
    print(output, flush=True)
    first_tick = False
