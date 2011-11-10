__author__ = 'vigo@vigo.su'

n = input("N=")
q = 0
while n>1 and q == 0:
    q = n%2
    n = n/2
    #print q
    #print n
    #print "--"
if n==1 and q == 0:
    print "YES"
else:
    print "NO"