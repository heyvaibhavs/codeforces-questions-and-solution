n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
c=0
for i in range(n):
    for j in range(m):
        z=0
        if i-1>=0 and j-1>=0 and a[i-1][j-1]>=a[i][j]:
            z=-1
        if i-1>=0 and a[i-1][j]>=a[i][j]:
            z=-1
        if i-1>=0 and j+1<m and a[i-1][j+1]>=a[i][j]:
            z=-1
        if j-1>=0 and a[i][j-1]>=a[i][j]:
            z=-1
        if j+1<m and a[i][j+1]>=a[i][j]:
            z=-1
        if i+1<n and j-1>=0 and a[i+1][j-1]>=a[i][j]:
            z=-1
        if i+1<n and a[i+1][j]>=a[i][j]:
            z=-1
        if i+1<n and j+1<m and a[i+1][j+1]>=a[i][j]:
            z=-1
        if z==0:
            c+=1
print(c)



