

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


def voda(qn,wn,li,o):
    q=0
    w=0
    qs=0
    ws=0
    if qn%a == 0 and qn!=0:
        q=a
        qs=qn/a-1
    else:
        q=qn%(a)
        qs=qn/a
    if wn%b ==0 and wn!=0:
        w=b
        ws=wn/b-1
    else:
        w=wn%b
        ws=wn/b

    liq= copy.deepcopy(li)
    listToSend = []
    nextStep =False
    if len(matrix[q][w])==0:
        liq.append([q,w,o])
        matrix[q][w] = copy.deepcopy(liq)
        nextStep = True
    elif len(matrix[q][w])>len(li):
        liq.append([q,w,o])
        matrix[q][w] = copy.deepcopy(liq)
        nextStep = True
        
    listToSend = copy.deepcopy(matrix[q][w])

    #1 >a
    if nextStep and q!=a:
        voda(a+ a*qs,w+b*ws,listToSend,1)
    #2 >b
    if nextStep and w!=b:
        voda(q+a*qs,b+b*ws,listToSend,2)
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
            voda(toq+a*qs,tow+b*ws,listToSend,3)

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
            voda(toqq+a*qs,toww+b*ws,listToSend,4)
    #5 a>
    if nextStep and q>0:
        voda(qs*a,w+b*ws,listToSend,5)
    #6 b>
    if nextStep and w>0:
        voda(q+a*qs,ws*b,listToSend,6)
    #7 a>c
    if nextStep and w>0:
        voda(a*(qs+1),w+b*ws,listToSend,7)
    #8 b>c
    if nextStep and w>0:
        voda(q+a*qs,(ws+1)*b,listToSend,8)

voda(0,0,[[-1,-1]],0)

flag=-1
flagList=[]

showMatrix(matrix)

if n<=a:
    for i in xrange(0,len(matrix[0]),1):
        if (len(matrix[n][i])<flag or flag==-1) and len(matrix[n][i])!=0:
            flag = len(matrix[n][i])
            flagList = copy.deepcopy(matrix[n][i])
if n<=b:
    for i in xrange(0,len(matrix),1):
        if (len(matrix[i][n])<flag or flag==-1) and len(matrix[i][n])!=0:
            flag = len(matrix[i][n])
            flagList = copy.deepcopy(matrix[i][n])

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




  