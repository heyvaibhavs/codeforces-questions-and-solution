for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    f=(n+1)*[0]
    for i in range(n):
        f[a[i]]+=1
    x,y=0,0
    for i in range(n+1):
        if f[i]>0:
            x+=1
        if f[i]>y:
            y=f[i]
    if x==y:
        print(x-1)
    else:
        print(min(x,y))
