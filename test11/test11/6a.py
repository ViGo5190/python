__author__ = 'vigo@vigo.su'

# -*- coding: utf-8 -*-

import re
import copy
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
    #print '!!!'
    #print table
    #print '!!'
    return table[l2][l1]



f = open('6.txt','r')
s1 = unicode(f.readline().strip(), 'utf-8')

print s1
s2 = unicode(f.readline().strip(), 'utf-8')
fuu = int(f.readline());
print fuu
strs = []
strs.append(s1)
for i in xrange(0,fuu,1):
    ss = unicode(f.readline().strip(), 'utf-8')
    strs.append(ss)
    print '!',strs[i],'!'
strs.append(s2)
f.close()
fuu +=2


#print lev(s1,s2)
print len(s1), '1',len(strs[2])
print lev(s1,strs[2])
print '--------------------------------------------------------'

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
words.append([s1])
print words[0][0]

for i in xrange(0,fuu,1):
    for j in xrange(0,fuu,1):
        print levmatrix[i][j],
    print
    
check = True
allfinish = False
while check:
    tempwords = copy.deepcopy(words)

    for lq in xrange(0,len(words),1):
        #print '======',lq
        check = False
        for i in xrange (0,len(strs),1):
            #print '----------',strs[i],' ',lq,' ',i,' ', words[lq][len(words[lq])-1]
            if strs[i]==words[lq][len(words[lq])-1]:
                for j in xrange (i+1,len(strs),1):
                    if levmatrix[i][j]==1:
                        if strs[i]==s2:
                            allfinish = True
                        print '->>>>>',strs[i],' ',lq,' ',i,' ',j,' ', words[lq][len(words[lq])-1]
                        tempstr = []
                        tempstr = copy.deepcopy(words[lq])
                        tempstr.append(strs[j])
                        levmatrix[i][j]=0
                        tempwords.append(tempstr)
                        check = True
                        print '^^^^',tempwords
                print '-<<<',words
    #print 'rere'
    if len(tempwords)>0:
        words = copy.deepcopy(tempwords)
    #print words
    #for i in xrange(0,fuu,1):
    #    for j in xrange(0,fuu,1):
    #        print levmatrix[i][j],
    #    print
    #check=False

print '---'
for i in xrange(0,len(words),1):
    if True:
        #print 'qwe'
        for j in xrange(0,len(words[i]),1):
            print words[i][j],
    print