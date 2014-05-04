#!/usr/bin/env python
# encoding: utf-8

aiueo = "aiueo"
with open("data/japanese.txt") as f:
    for line in f:
        line = line.strip()
        if len(line) > 0 and line[0] in aiueo:
            print line[0]+"".join([s for s in line[1:] if s not in aiueo])
        else:
            print "".join([s for s in line if s not in aiueo])
