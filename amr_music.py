n,k=map(int,input().split())
a=list(map(int,input().split()))
l=a[:]
a.sort()
x,c=0,0
for i in range(n):
    x+=a[i]
    if x<k:
        c+=1
    else:
        if k-x>=0:
            c=c+1
        break
print(c)
for i in range(c):
    x=l.index(a[i])
    print(x+1,end=" ")
    l[x]=-1
    