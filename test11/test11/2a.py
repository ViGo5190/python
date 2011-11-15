__author__ = 'vigo@vigo.su'
import copy
a = input("A=")
b = input("B=")
n = input("N=")

#a=3
#b=5
#n=9

an = 0
bn = 0

if n%a != 0:
    an = (n/a + 1)*a
else:
    an = n

if n%b != 0:
    bn = (n/b +1)*b
else:
    bn = n
print an, bn


qmatrix = []
for i in xrange(0,a+1,1):
    row = []
    for j in xrange(0,b+1,1):
        col= []
        row.append(col)


    qmatrix.append(row)

def showQQMatrix():
    for ii in xrange(0, len(qqmatrix),1):
        for i in xrange(0,a+1,1):
            for jj in xrange(0,len(qqmatrix[0]),1):
                for j in xrange(0,b+1,1):
                    print len(qqmatrix[ii][jj][i][j]),' |',
            print

matrix = copy.deepcopy(qmatrix)
qqmatrix = []

for i in xrange(0, (an/a)+1,1):
    itrow = []
    for j in xrange(0,(bn/b)+1,1):
        myline = []
        myline = copy.deepcopy(matrix)
        itrow.append(myline)
    qqmatrix.append(itrow)



def voda(q,qs,w,ws,li,o):

    qn=q+qs*a
    wn=w+ws*b


    liq= copy.deepcopy(li)
    listToSend = []
    nextStep =False
    if len(qqmatrix[qs][ws][q][w])==0:
        liq.append([q,w,o])
        qqmatrix[qs][ws][q][w] = copy.deepcopy(liq)
        nextStep = True
    elif len(qqmatrix[qs][ws][q][w])>len(li):
        liq.append([q,w,o])
        qqmatrix[qs][ws][q][w] = copy.deepcopy(liq)
        nextStep = True

    listToSend = copy.deepcopy(qqmatrix[qs][ws][q][w])


    #1 >a
    if nextStep and q!=a :
        voda(a, qs,w,ws,listToSend,1)
    #2 >b
    if nextStep and w!=b:
        voda(q,qs,b,ws,listToSend,2)
    #3 a>b
    if q!=0 and w<b:
        toq = 0
        tow = 0
        if (q+w) >= b:
            tow = b
            toq = q+w-b
        else:
            tow = q+w
            toq = 0

        if nextStep and (q+w)!=b:
            #print toq,tow
            voda(toq,qs,tow,ws,listToSend,3)

    #4 b>a
    if w!=0 and q<a:
        toqq = 0
        toww = 0
        if (q+w) >= a:
            toww = q+w-a
            toqq = a
        else:
            toww = 0
            toqq = q+w
        if nextStep and (q+w)!=a:
            voda(toqq,qs,toww,ws,listToSend,4)
    #5 a>
    if nextStep and q>0:
        voda(0,qs,w,ws,listToSend,5)
    #6 b>
    if nextStep and w>0:
        voda(q,qs,0,ws,listToSend,6)
    #7 a>c
    if nextStep and q>0 and ((qs+1)*a)<an:
        voda(0,qs+1,w,ws,listToSend,7)
    #8 b>c
    if nextStep and w>0 and ((ws+1)*b)<bn:
        voda(q,qs,0,(ws+1),listToSend,8)

voda(0,0,0,0,[[-1,-1]],0)

flag=-1
flagList=[]


showQQMatrix()

lastPrint =""

if n<=an or n<=bn:
    for ii in xrange(0,len(qqmatrix),1):
        for jj in xrange(0,len(qqmatrix[0]),1):
            for i in xrange(0, a+1,1):
                for j in xrange(0,b+1,1):
                    if (ii*a+jj*b+i)==n and len(qqmatrix[ii][jj][i][j])!=0 and (len(qqmatrix[ii][jj][i][j])<flag or flag==-1):
                        flag = len(qqmatrix[ii][jj][i][j])
                        flagList = copy.deepcopy(qqmatrix[ii][jj][i][j])
                        lastPrint = "A>C"
                    if (ii*a+jj*b+j)==n and len(qqmatrix[ii][jj][i][j])!=0 and (len(qqmatrix[ii][jj][i][j])<flag or flag==-1):
                        flag = len(qqmatrix[ii][jj][i][j])
                        flagList = copy.deepcopy(qqmatrix[ii][jj][i][j])
                        lastPrint = "B>C"


            

print flag
print flagList
if len(flagList)>2:
    for i in xrange(2,len(flagList),1):
        if flagList[i][2] == 1:
            print '>A'
        if flagList[i][2] == 2:
            print '>B'
        if flagList[i][2] == 3:
            print 'A>B'
        if flagList[i][2] == 4:
            print 'B>A'
        if flagList[i][2] == 5:
            print 'A>'
        if flagList[i][2] == 6:
            print 'B>'
        if flagList[i][2] == 7:
            print 'A>C'
        if flagList[i][2] == 8:
            print 'B>C'
    print lastPrint
else:
    print 'Impossible'




