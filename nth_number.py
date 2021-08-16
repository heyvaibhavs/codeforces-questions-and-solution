import math
def nu(n):
    if n==1:
        return 1 
    return 10**(n-1)+9*nu(n-1)
n=int(input())
x=math.log(n, 9)
# print(x)
if n<9:
    print(n)
else:
    y=nu(int(x))
    print(y)
    if x-int(x)==0:
        print(n+y)
    else:
        z=10**int(x)-y
        print(n+y+(n-z)//9)