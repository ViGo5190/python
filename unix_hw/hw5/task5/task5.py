import cmath

N = input("Specified n: ")
Pi = cmath.pi
qwe = set()
for i in range (0,N):
    d = cmath.cos(2*Pi*i/N)
    m = -cmath.sin(2*Pi*i/N)
    c = complex( d , m )
    qwe.add(c)

print qwe
