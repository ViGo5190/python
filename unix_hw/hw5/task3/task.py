import math

def primes(N):
    #RESHETO
    sieve = set(range(2, N))
    for i in range(2, int(math.sqrt(N))):
        if i in sieve:
            sieve -= set(range(2*i, N, i))
    return sieve

def checkit(N):
    #hw
    ar = primes(N)
    lenght = len(ar)
    qwe = set() 
    for i in range (1,N+1):
        arr = primes(int(math.sqrt(i))+1)
        for j in arr:
            a = i/j
            b = i%j
            if b==0:
                if a in ar:
                    #qwe += set([a])
                    qwe.add(i)
                    print '%d = %d * %d' % (i,a,j)
    return qwe

print "---"
print checkit(11)
print "---"

"""
primearray =  primes(100)
print len(primearray)
if 3 in primearray:
    print "k"
for i in primearray:
    print i    
print primearray

s = set(range(2, 6))

s = s - set(range(4,5))

print s

k = set(range(3, 15 ,2))
print k
k -= set(range(3,4))
print k
"""
