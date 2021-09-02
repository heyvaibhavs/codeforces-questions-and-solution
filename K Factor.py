n,k=map(int,input().split())
l=[]
i=2
while i<n:
    if n%i==0:
        l.append(i)
        n=n//i
    else:
        i+=1
if n>1:
    l.append(n)
# print(l)
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
