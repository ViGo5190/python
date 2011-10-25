import math

def primes(N):
    sieve = set(range(2, N))
    for i in range(2, int(math.sqrt(N))):
        if i in sieve:
            sieve -= set(range(2*i, N, i))
            return sieve
print primes(10)
