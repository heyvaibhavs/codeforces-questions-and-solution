import math
n=int(input())
x=(-1+ math.sqrt(1+8*n))//2
y=x*(x+1)//2
if n-y==0:
    print(int(x))
else:
    print(int(n-y))


