#!/usr/bin/env python
# encoding utf-8

import string
_aZ=string.ascii_letters
_09="0123456789"
_sp="_?><+*}{`|~=~)('&%$#\"!-^\[@]:;,./\\"

digits=range(2,9)

many = _aZ+_09+_sp

print "\n".join([s * digit for s in many for digit in digits])
