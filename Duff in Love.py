# Code by : Sam._.072

import math
n = int(input())
z=0
x=int(math.sqrt(n))
i=2
while i <= x:
    if i*i>n:
        break
    elif n%(i*i)==0:
        n=n//i
    else:
        i+=1


print(n)
