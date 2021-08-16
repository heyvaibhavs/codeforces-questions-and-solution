n,d=map(int,input().split())
a=list(map(int,input().split()))
# print(sorted(a))
f=100005*[0]
for i in range(n):
    f[a[i]]+=1
c=0
for i in range(n):
    c+=f[d-a[i]]
    if d-a[i]==a[i]:
        c-=1


print(c//2)

