for _ in range(int(input())):
    n,m=map(int,input().split())
    r=n*[0]
    c=m*[0]
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(m):
            if a[i][j]==1:
                r[i]=1
                c[j]=1
    x,y=r.count(1),c.count(1)
    if x==n or y==m:
        k=0
    else:
        k=min(n-x,m-y)
    if k%2!=0:
        print("Ashish")
    else:
        print("Vivek")