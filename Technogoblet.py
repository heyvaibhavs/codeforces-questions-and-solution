n,m,k=map(int,input().split())
p=list(map(int,input().split()))
s=list(map(int,input().split()))
a=list(map(int,input().split()))
f=(m+1)*[0]
for i in range(n):
    if f[s[i]]<p[i]:
        f[s[i]]=p[i]
c=0
for i in range(k):
    for j in range(1,m+1):
        if a[i] == f[j]:
            f[j]=0
            c+=1
            break
        
print(k-c)



