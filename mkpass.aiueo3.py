#!/usr/bin/env python
# encoding utf-8

import string
a2z = string.lowercase
aiueo = "aiueo"
print "\n".join([s1+a1+s2+a2 for s1 in a2z\
                             for a1 in aiueo\
                             for s2 in a2z\
                             for a2 in aiueo])
