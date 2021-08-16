n,m=map(int,input().split())
s=input()
t=input()
h,ans=m+2,[]
for i in range(m-n+1):
    c,l=0,[]
    for j in range(n):
        if s[j]!=t[i+j]:
            c+=1
            l.append(j+1)
    if c<h:
        h=c
        ans=l
print(h)
print(*ans)

