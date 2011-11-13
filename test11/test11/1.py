import copy

__author__ = 'vigo@vigo.su'
import copy
#a = input("A")
#b = input("B")
#n = input("N")

a=3
b=5
n=1

qmatrix = []
for i in xrange(0,a+1,1):
    row = []
    for j in xrange(0,b+1,1):
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

#showMatrix(qmatrix)

#isRun = True

#while isRun:


def vod(q,w,li,o,myqwe):
    matrix = copy.deepcopy(myqwe)
    nextStep =False
    if len(matrix[q][w])==0:
        #rows = []
        #rows = copy.deepcopy(matrix[q][w])
        #rows.append(li)
        li.append([q,w,o])
        matrix[q][w] = copy.deepcopy(li)
        #matrix[q][w] = copy.deepcopy(rows)
        nextStep = True
    if len(matrix[q][w])>len(li):
        matrix[q][w] = matrix[q][w] + li
        nextStep = True
    listToSend = copy.deepcopy(matrix[q][w])

    print '---'
    print listToSend
    showMatrix(matrix)



    #if q!=5 :
    #    print "start"
    #    vod(5,0,listToSend,1)

    #1 >a
    if nextStep:
        vod(a,w,listToSend,1,matrix)
    #2 >b
    if nextStep:
        vod(q,b,listToSend,2,matrix)
    #3 a>b
    if q+w >= b:
        tow = b
        toq = q+w-b
    if q+w <= b:
        tow = q+w
        toq = 0
    if nextStep:
        vod(toq,tow,listToSend,3,matrix)

    #4 b>a
    if q+w >= a:
        tow = q+w-a
        toq = a
    if q+w <= a:
        tow = 0
        toq = q+w
    if nextStep:
        vod(toq,tow,listToSend,4,matrix)
    #5 a>
    if nextStep:
        vod(0,w,listToSend,5,matrix)
    #6 b>
    if nextStep:
        vod(q,0,listToSend,6,matrix)

    #isRun = False


#vod(0,0,[[-1,-1]],0,qmatrix)

matrix = copy.deepcopy(qmatrix)


def voda(q,w,li,o):
    
    listToSend = []
    nextStep =False
    if len(matrix[q][w])==0:
        li.append([q,w,o])
        matrix[q][w] = copy.deepcopy(li)
        nextStep = True
    if len(matrix[q][w])>len(li):
        li.append([q,w,o])
        matrix[q][w] = copy.deepcopy(li)
        nextStep = True
        
    listToSend = copy.deepcopy(matrix[q][w])


    #print '---'
    #print listToSend
    #showMatrix(matrix)
    #if not nextStep:
    #    print 'STOP'


    #if q!=5 :
    #    print "start"
    #    vod(5,0,listToSend,1)

    #1 >a
    if nextStep and q!=a:
        voda(a,w,listToSend,1)
    #2 >b
    if nextStep and w!=b:
        voda(q,b,listToSend,2)
    #3 a>b
    if q!=0 and w<b:
        toq = 0
        tow = 0
        print '--'
        print toq,tow,q,w,a,b
        if (q+w) >= b:
            tow = b
            toq = q+w-b
        else:
            tow = q+w
            toq = 0

        if nextStep and (q+w)!=b:
            print toq,tow
            voda(toq,tow,listToSend,3)

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
            voda(toqq,toww,listToSend,4)
    #5 a>
    if nextStep and q>0:
        voda(0,w,listToSend,5)
    #6 b>
    if nextStep and w>0:
        voda(q,0,listToSend,6)

    #isRun = False
voda(0,0,[[-1,-1]],0)

showMatrix(matrix)

flag=-1
flagList=[]

print '====='

if n<=a:
    for i in xrange(0,len(matrix[0]),1):
        if (len(matrix[n][i])<flag or flag==-1) and len(matrix[n][i])!=0:
            flag = len(matrix[n][i])
            print flag,'a'
            flagList = copy.deepcopy(matrix[n][i])
if n<=b:
    print 'len=', len(matrix)
    for i in xrange(0,len(matrix),1):
        if (len(matrix[i][n])<flag or flag==-1) and len(matrix[i][n])!=0:
            print flag,'b'
            flag = len(matrix[i][n])
            flagList = copy.deepcopy(matrix[i][n])
print '====='
print flag
print flagList
if len(flagList)>2:
    for i in xrange(2,len(flagList),1):
        if flagList[i][2] == 1:
            print '>a'
        if flagList[i][2] == 2:
            print '>b'
        if flagList[i][2] == 3:
            print 'a>b'
        if flagList[i][2] == 4:
            print 'b>a'
        if flagList[i][2] == 5:
            print 'a>'
        if flagList[i][2] == 6:
            print 'b>'

#isDo = True

print matrix[0][1]

#while isDo:
#    for i in xrange(0,len(matrix),1):
#        for j in xrange(0,len(matrix[i]),1):
#            if True:
#                print 1
#    isDo=false



#showMatrix(matrix)

  