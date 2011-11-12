import copy

__author__ = 'vigo@vigo.su'
import copy
#a = input("A")
#b = input("B")
#n = input("N")

a=5
b=8
n=3

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
            if len(matrix[i][j])>0:
                print '1 |',
            else:
                print '0 |',
        print

showMatrix(qmatrix)

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


vod(0,0,[[-1,-1]],0,qmatrix)


  