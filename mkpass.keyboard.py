#!/usr/bin/env python
# encoding: utf-8

#keyboard = ['!"#$%&\'()~=~',
keyboard = ['1234567890-^',
            'qwertyuiop@[',
            'asdfghjkl;:]',
            'zxcvbnm,./\\']
#12x1 +
#12x4

def LR(num):
    """
    Left to Right
    """
    for line in keyboard:
        for i in range(len(line)):
            ret = line[i:i+num]
            if len(ret)<num:
                break
            yield ret
def RL(num):
    """
    Right to Left
    """
    for line in LR(num):
        yield line[::-1]
def UD(num):
    """
    Up to Down
    """
    for ret in ["".join(zipped) for zipped in zip(*keyboard)]:
        yield ret[:num]

def DU(num):
    """
    Up to Down
    """
    for ret in ["".join(zipped) for zipped in zip(*keyboard)]:
        yield ret[::-1][:num]

qwer = LR(4)
qwe = LR(3)
rewq= RL(4)
rew= RL(3)
_1qaz = UD(4)
_1qa = UD(3)
zaq1 = DU(4)
zaq = DU(3)


#ULR DRL loop
qwsa = ['12wq', '23ew', '34re', '45tr', '56yt', '67uy', '78iu', '89oi', '90po', '0-@p',
          '-^@p', '^\\[@', 'qwsa', 'weds', 'erfd', 'rtgf', 'tyhg', 'yujh', 'uikj', 'iolk',
          'op;l', 'p@:;', '@[]:', 'asxz', 'sdcx', 'dfvc', 'fgbv', 'ghnb', 'hjmn', 'jk,m',
          'kl.,', 'l;/.', ';:\\/', ':]\\/']
wsaq = [qwsa_[1:]+qwsa_[0] for qwsa_ in qwsa]
saqw = [qwsa_[2:]+qwsa_[:2] for qwsa_ in qwsa]
aqws = [qwsa_[-1]+qwsa_[0:-1] for qwsa_ in qwsa]

#DLR URL loop
aswq = [qwsa_[::-1] for qwsa_ in qwsa]
swqa = [aswq_[1:]+aswq_[0] for aswq_ in aswq]
wqas = [aswq_[2:]+aswq_[:2] for aswq_ in aswq]
qasw = [aswq_[-1]+aswq_[0:-1] for aswq_ in aswq]

everywhere=['Az"%s"','>0A[0]"%s"','>1A[1]"%s"','>2A[2]"%s"','>3A[3]"%s"','>4A[4]"%s"','>5A[5]"%s"','>6A[6]"%s"','>7A[7]"%s"','>8A[8]"%s"','>9A[9]"%s"']
#for i in range(10):
for lines in qwer,qwe,rewq,rew,_1qaz,_1qa,zaq1,zaq,qwsa,wsaq,saqw,aqws,aswq,swqa,wqas,qasw:
    for line in lines:
        print line

