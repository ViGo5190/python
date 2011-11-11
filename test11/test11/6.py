__author__ = 'vigo@vigo.su'
# -*- coding: utf-8 -*-
import re

#p = re.compile('(ab[a-z]?b)',re.IGNORECASE)
#reg =  p.search("abnb")
#if reg:
#    print reg.group(),' ',reg.span()

f = open('6.txt','r')
s1 = f.readline().strip()
s1 = unicode(s1,'utf-8').encode('utf-8')
print s1
s2 = f.readline()
s2 = unicode(s2,'utf-8').encode('utf-8')
fuu = int(f.readline());
print fuu
strs = []
for i in xrange(0,fuu,1):
    ss = f.readline().strip()
    ss = unicode(ss, 'utf-8').encode('utf-8')
    strs.append(ss)
    print '!',strs[i],'!'
    
f.close()

words = []
words.append([s1])
print words[0]

sq = strs[0]
print len(sq)
print sq[4::]
print sq[:-6:]+'[a-z]?'+sq[::]
print sq[:-4:]+'[a-z]?'+sq[2::]
print sq[:-2:]+'[a-z]?'+sq[4::]
print sq[::]+'[a-z]?'+sq[6::]

rrr = sq[:-2:]+'\W?'+sq[4::]
pp = re.compile(rrr,re.IGNORECASE)
reg2 = pp.search(sq)
if reg2:
    print reg2.group(),' ',reg2.span()

print '----'
while True:
    tempwords = []
    for i in xrange(0,len(words),1):
        print words[i]
        le = len(words[i])-1
        tempstr = words[i][len(words[le])-1]


        print tempstr
        find = False


        tempregexp = '\w?'+tempstr[::]
        tempregexp = tempregexp.strip()
        ptemp = re.compile(tempregexp, re.IGNORECASE)
        print '-'
        print tempregexp
        valToDel = []
        for j in xrange(0,len(strs),1):
            #print strs[j] + ' !' + tempregexp+'! '
            regtemp = ptemp.search(strs[j])
            if regtemp:
                print regtemp.group(),' ',regtemp.span(),' ',strs[j]
                find = True
                qwe = words[i]
                qwe.append(strs[j])
                tempwords.append(qwe)
                valToDel.append(strs[j])
        print '+'
        for regi in xrange(2,len(tempstr),2):
            regimin = (-1)*len(tempstr) + regi
            tempregexp = tempstr[:regimin:]+'\w'+tempstr[regi::]
            tempregexp = tempregexp.strip()
            ptemp = re.compile(tempregexp, re.IGNORECASE)
            print '-'
            print tempregexp
            for j in xrange(0,len(strs),1):
                #print strs[j] + ' !' + tempregexp+'! '
                regtemp = ptemp.search(strs[j])
                if regtemp:
                    print regtemp.group(),' ',regtemp.span(),' ',strs[j]
                    find = True
                    qwe = words[i]
                    qwe.append(strs[j])
                    tempwords.append(qwe)
                    valToDel.append(strs[j])
        print '-?'
        for regi in xrange(2,len(tempstr),2):
            regimin = (-1)*len(tempstr) + regi
            tempregexp = tempstr[:regimin-2:]+"\w"+tempstr[regi::]
            tempregexp = tempregexp.strip()
            ptemp = re.compile(tempregexp, re.IGNORECASE)
            print '-'
            print [tempregexp]
            for j in xrange(0,len(strs),1):
                #print strs[j] + ' !' + tempregexp+'! '
                regtemp = ptemp.search(strs[j])
                #print '-----------------',strs[j]
                if regtemp:
                    print regtemp.group(),' ',regtemp.span(),' ',strs[j]
                    find = True
                    qwe = words[i]
                    qwe.append(strs[j])
                    tempwords.append(qwe)
                    valToDel.append(strs[j])

        for delli in xrange(0,len(valToDel),1):
            strs.remove(valToDel[delli])



    print tempwords
    words = tempwords
    break