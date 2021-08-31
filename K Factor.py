n,k=map(int,input().split())
l=[]
for i in range(2,n//2+1):
    if n%i==0:
        l.append(i)
if k>len(l):
    print(-1)
else:
    n1=len(l)
    p=1
    for i in range(n1-k+1):
        p=p*l[i]
    print(p,end=" ")
    for i in range(n1-k+1,n1):
        print(l[i],end=" ")
