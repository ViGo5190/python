

__author__ = 'vigo@vigo.su'
import copy
#a = input("A=")
#b = input("B=")
#n = input("N=")

a=3
b=5
n=6

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

qmatrix = []
for i in xrange(0,an+1,1):
    row = []
    for j in xrange(0,bn+1,1):
        col= []
        row.append(col)
    
    
    qmatrix.append(row)

def showMatrix(qwe):
    matrix = copy.deepcopy(qwe)
    for i in xrange(0,len(matrix),1):
        for j in xrange(0,len(matrix[i]),1):
            #print matrix[i][j], '| ',
            print len(matrix[i][j]),' |',
            #if len(matrix[i][j])>0:
            #    print '1 |',
            #else:
            #    print '0 |',
        print


matrix = copy.deepcopy(qmatrix)


def voda(q,qs,w,ws,li,o):

    #q=0
    #w=0
    #qs=0
    #ws=0
    qn=q+qs*a
    wn=w+ws*b
    print q, qn,w, wn ,'li', o ,qs,ws
    #if qn%a == 0 and qn!=0:
    #    q=a
    #    qs=qn/a-1
    #else:
    #    q=qn%(a)
    #    qs=qn/a
    #if wn%b ==0 and wn!=0:
    #    w=b
    #    ws=wn/b-1
    #else:
    #    w=wn%b
    #    ws=wn/b

    liq= copy.deepcopy(li)
    listToSend = []
    nextStep =False
    if len(matrix[qn][wn])==0:
        liq.append([q,w,o])
        matrix[qn][wn] = copy.deepcopy(liq)
        nextStep = True
    elif len(matrix[qn][wn])>len(li):
        liq.append([q,w,o])
        matrix[qn][wn] = copy.deepcopy(liq)
        nextStep = True
        
    listToSend = copy.deepcopy(matrix[qn][wn])

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
    if nextStep and q>0 and ((qs+1)*a)<=an:
        voda(0,qs+1,w,ws,listToSend,7)
    #8 b>c
    if nextStep and w>0 and ((ws+1)*b)<=bn:
        voda(q,qs,0,(ws+1),listToSend,8)

voda(0,0,0,0,[[-1,-1]],0)

flag=-1
flagList=[]

showMatrix(matrix)

if n<=an:
    for i in xrange(0,len(matrix[0]),1):
        if (len(matrix[n][i])<flag or flag==-1) and len(matrix[n][i])!=0:
            flag = len(matrix[n][i])
            flagList = copy.deepcopy(matrix[n][i])
if n<=bn:
    for i in xrange(0,len(matrix),1):
        if (len(matrix[i][n])<flag or flag==-1) and len(matrix[i][n])!=0:
            flag = len(matrix[i][n])
            flagList = copy.deepcopy(matrix[i][n])
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
else:
    print 'Impossible'




  