n,a,b=map(int,input().split())
if n==1:
    print(1)
elif b==0:
    print(a)
elif b>0:
    if (a+b)%n==0:
        n=n
    else:
        n=(a+b)%n
    print(n)
else:
    b=abs(b)
    b=b-(a-1)
    b=b%n
    if b==0:
        print(1)
    else:
        print(n-b+1)