for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    d=dict()
    for i in range(n):
        d[a[i]]=1
    for i in range(n,n+m):
        # print(a[i])
        if a[i] in d:
            print("YES")
        else:
            print("NO")
            d[a[i]]=1



