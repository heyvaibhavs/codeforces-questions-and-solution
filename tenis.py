n,a,p=map(int,input().split())
c,x=0,n
while n>=2:
    if n%2==0:
        c+=n//2
        n=n//2
    else:
        c+=n//2
        n=n//2+1
print(c*(2*a+1),p*x)



