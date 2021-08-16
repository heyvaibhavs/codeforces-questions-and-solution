n,m=map(int,input().split())
c=0
for i in range(n):
    a=list(map(int,input().split()))
    if i==0 and 1 in a:
        c=1
    elif i==n-1 and 1 in a:
        c=1
    elif a[0]==1 or a[m-1]==1:
        c=1        
if c==1:
    print(2)
else:
    print(4)



