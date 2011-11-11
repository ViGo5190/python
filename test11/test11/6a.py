__author__ = 'vigo@vigo.su'

# -*- coding: utf-8 -*-

import re

def lev(word1, word2) :
    l1 = len(word1)
    l2 = len(word2)

    table = [range(l1 + 1)] * (l2 + 1)
    for zz in range(l2 + 1) :
        table[zz] = range(zz,zz + l1 + 1)
    for zz in range(0,l2) :
        for sz in range(0,l1) :
            if word1[sz] == word2[zz] :
                table[zz+1][sz+1] = min(table[zz+1][sz] + 1, table[zz][sz+1] + 1, table[zz][sz])
            else :
                table[zz+1][sz+1] = min(table[zz+1][sz] + 1, table[zz][sz+1] + 1, table[zz][sz] + 1)
    return table[l2][l1]



f = open('6.txt','r')
s1 = f.readline().strip()

print s1
s2 = f.readline().strip()
fuu = int(f.readline());
print fuu
strs = []
strs.append(s1)
for i in xrange(0,fuu,1):
    ss = f.readline().strip()
    strs.append(ss)
    print '!',strs[i],'!'
strs.append(s2)
f.close()



print lev(s1,s2)

levmatrix = []

for i in xrange(0,fuu,1):
    levrow =[]
    for j in xrange(0,fuu,1):
        if i==j:
            levrow.append(0)
        else:
            levrow.append(lev(strs[i],strs[j]))
    print levrow
    levmatrix.append(levrow)


#print levmatrix
words = []
words.append(strs[0])
print words[0]

for i in xrange(0,fuu,1):
    tempwords = []
    for j in xrange(i,fuu,1):
        if levmatrix[i][j]==1:
            
            print '1'

while True:
    tempwords = []
    for lq in xrange(0,len(words),1):
        for i in xrange (0,len(strs),1):
            print strs[i],
            if strs[i]==words[lq][len(words[lq])-1]:
                for j in 
                print 'rere'
    break