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
    ss = f.readline().strip()
    strs.append(ss)
    print '!',strs[i],'!'
    
f.close()

words = []
words.append([0,s1])
print words[0][1]

sq = strs[0]

print sq[4::]
print sq[:-6:]+'[a-z]?'+sq[::]
print sq[:-4:]+'[a-z]?'+sq[2::]
print sq[:-2:]+'[a-z]?'+sq[4::]
print sq[::]+'[a-z]?'+sq[6::]

rrr = sq[:-2:]+'[a-z]?'+sq[4::]
pp = re.compile(rrr,re.IGNORECASE)
reg2 = pp.search(sq)
if reg2:
    print reg2.group(),' ',reg2.span()


while True:

    break