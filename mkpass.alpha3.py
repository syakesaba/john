#!/usr/bin/env python
# encodin: utf-8

import string
aZ=string.ascii_letters
print "\n".join([s1+s2+s3 for s1 in aZ for s2 in aZ for s3 in aZ])

