__author__ = 'vigo@vigo.su'

#a = input("A")
#b = input("B")
#n = input("N")

a=5
b=8
n=3

matrix = []
for i in xrange(0,a,1):
    row = []
    for j in xrange(0,b,1):
        col= []
        row.append(col)
    
    
    matrix.append(row)

def showMatrix():
    for i in xrange(0,len(matrix),1):
        for j in xrange(0,len(matrix[i]),1):
            print matrix[i][j], '| ',
        print

showMatrix()

isRun = True

while isRun:
    def vod(q,w):
        if len(matrix[q][w])==0:
            matrix[q][w].append(1)
    isRun = False
vod(0,0)

print '---'
showMatrix()
  