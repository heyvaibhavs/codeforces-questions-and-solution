for _ in range(int(input())):
    n,t=map(int,input().split())
    a=list(map(int,input().split()))
    x,p=[],0
    for i in range(n):
        if a[i]<t/2:
            x.append(0)
        elif a[i]==t//2:
            if p==0:
                x.append(1)
                p=1
            else:
                x.append(0)
                p=0
        else:
            x.append(1)
    print(*x)
