n=int(input())
a=list(map(int,input().split()))
l,h=list(set(a)),0
f=max(l)*[0]
for i in range(n):
    f[a[i]-1]+=1
    if f[a[i]-1]>h:
        h=f[a[i]-1]
f=None
f=max(l)*[0]
for i in range(n):
    f[a[i]-1]+=1
    if f[a[i]-1]==h:
        print(a[i])
        break
    




