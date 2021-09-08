# problem name : Elections
# problem link : https://codeforces.com/problemset/problem/570/A
# Rating : 1100

n,m=map(int,input().split())
l=n*[0]
for k in range(m):
    a=list(map(int, input().split()))
    h,j=-1,-1
    for i in range(n):
        if a[i]>h:
            h=a[i]
            j=i
    l[j]+=1
h,j=-1,-1
for i in range(n):
    if l[i]>h:
        h=l[i]
        j=i
print(j+1)
