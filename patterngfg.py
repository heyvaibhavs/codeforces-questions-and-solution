n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
x=y=0
for j in range(m-1,-1,-1):
    if x==0:
        for i in range(n):
            print(a[i][j],end=" ")
        x=-1
    else:
        for i in range(n-1,-1,-1):
            print(a[i][j],end=" ")
        x=0
