import math
n=int(input())
if n<=9:
    print(n)
else:
    l=int(math.log(n,10))
    if n%100==0:
        l-=1
    x=(10**l)-1
    c=l*9
    n=n-x
    while n>0:
        c+=n%10
        n=n//10
    print(c)
    