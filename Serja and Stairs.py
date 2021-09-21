# problem name : Serja and Stairs
# problem link : https://codeforces.com/problemset/problem/381/B
# Rating : 1100

n=int(input())
a=list(map(int, input().split()))
h=max(a)
f=(h+1)*[0]
for i in range(n):
    f[a[i]]+=1
c=0
for i in range(h):
    if f[i]>=2:
        c+=2
    else:
        c+=f[i]
c+=1
print(c)
l=(c)*[0]
i=0
j=c-1
# print(f)
for k in range(1,h+1):
    if k==h:
        l[i]=k
        i+=1
    elif f[k] >= 2:
        l[i]=k
        l[j]=k
        i+=1
        j-=1
    elif f[k]==1:
        l[i]=k
        i+=1
del a
del f
print(*l)
