n,k=map(int,input().split())
a=list(map(int, input().split()))
x=sum(a)
if x%k==0:
    x=x//k
    c=c1=0
    l=[]
    for i in range(n):
        c1+=a[i]
        c+=1
        if c1==x:
            l.append(c)
            c=c1=0
        elif c1>x:
            c=-1
            break
    if c==-1:
        print("No")
    else:
        print("Yes")
        print(*l)    
else:
    print("No")


