#!/usr/bin/env python
# encoding: utf-8

import re
r = re.compile(r"^(\d+)年.*$")
with open("data/nihonsi.nengou.txt") as f:
    for line in f:
        line = line.strip()
        matched = r.match(line)
        if matched:
            print matched.group(1)
