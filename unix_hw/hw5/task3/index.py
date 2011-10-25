#encoding:utf8
import math

a = input("Enter number: ")
#print a**2
b = a/2 +1;

p=[b] #пустой список f*ck
p[1]=1
counter = 1;
for i in range (2,a+1):
    for j in range (1,counter+1):
        c = i/j
        d = i%j
        if d==0:
            if c==i:
                p[counter] = i
                counte = counter+1
                print '%d = %d * %d' % ( i, c * j)
                break
            #for k in range(0,counter)
            #    if 

