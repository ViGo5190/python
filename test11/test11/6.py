__author__ = 'vigo@vigo.su'

import re

p = re.compile('(ab[a-z]?b)',re.IGNORECASE)
reg =  p.search("abnb")
if reg:
    print reg.group(),' ',reg.span()

f = open('6.txt','r')
s1 = f.readline()
s2 = f.readline()
fuu = int(f.readline());
print fuu
strs = []
for i in xrange(0,fuu,1):
    ss = f.readline()
    strs.append(ss)
    print strs[i]
f.close()
