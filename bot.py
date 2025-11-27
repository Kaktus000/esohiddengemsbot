#!/usr/bin/env python3
import sys, json, random, chefint
print("inited", flush=True, file=sys.stderr)
random.seed(1)
first_tick = True

for line in sys.stdin:
    data = json.loads(line)
    if first_tick:
        config = data.get("config", {})
        width = config.get("width")
        height = config.get("height")
        print("inited", flush=True, file=sys.stderr)
    cheffile = open("bot.chef")
    print(cheffile.read(), flush=True, file=sys.stderr)
    c = chefint.Chef(cheffile.read())
    output = c.cook()
    print(output, flush=True, file=sys.stderr)
    print(output, flush=True)
    first_tick = False
