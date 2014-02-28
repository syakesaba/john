#!/usr/bin/env python
# encoding utf-8

a2z = "akstnhmyrwgzdbpj"
aiueo = "aiueo"
print "\n".join([s1+a1+s2+a2+s3+a3 for s1 in a2z\
                             for a1 in aiueo\
                             for s2 in a2z\
                             for a2 in aiueo\
                             for s3 in a2z\
                             for a3 in aiueo])
