n,m=map(int,input().split())
a,b,c,d=1,2,2*n+1,2*n+2
for i in range(n):
    if c<=m:
        print(c,end=" ")
        c+=2
    if a<=m:
        print(a,end=" ")
        a+=2
    if d<=m:
        print(d,end=" ")
        d+=2
    if b<=m:
        print(b,end=" ")
        b+=2
        