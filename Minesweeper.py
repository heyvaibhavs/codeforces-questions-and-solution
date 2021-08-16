# problem link : https://codeforces.com/problemset/problem/984/B
# problem name : Minesweeper 
# point : (1100)

def neigh(a,i,j,n,m):
    c=0
    if j-1>=0 and a[i][j-1]=='*':
        c+=1
    if j+1<m and a[i][j+1]=='*':
        c+=1
    if i-1>=0 and a[i-1][j]=='*':
        c+=1
    if i+1<n and a[i+1][j]=='*':
        c+=1
    if i-1>=0 and j-1>=0 and a[i-1][j-1]=='*':
        c+=1
    if i-1>=0 and j+1<m and a[i-1][j+1]=='*':
        c+=1
    if i+1<n and j-1>=0 and a[i+1][j-1]=='*':
        c+=1
    if i+1<n and j+1<m and a[i+1][j+1]=='*':
        c+=1
    # print(i,j,c)
    return c

n,m=map(int,input().split())
a=[]
z=0
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(m):
        if ord(a[i][j])>=49 and ord(a[i][j])<=56:
            if neigh(a, i, j, n, m)!=int(a[i][j]):
                z=-1
                break
        elif a[i][j]=='.':
            if neigh(a, i, j, n, m)!=0:
                z=-1
                break
if z==0:
    print("YES")
else:
    print("NO")