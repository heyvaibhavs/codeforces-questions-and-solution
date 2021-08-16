n=int(input())
a=list(map(int,input().split()))
h=0
for i in range(n):
    if a[i]>h:
        h=a[i]
c1=c=0
for i in range(n):
    if a[i]==h:
        c1+=1
    else:
        if c1>c:
            c=c1
        c1=0
if c1>c:
    c=c1
print(c)
