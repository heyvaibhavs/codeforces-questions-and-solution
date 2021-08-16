n=int(input())
a=list(map(int, input().split()))
h=max(a)
t,m=1,10000000
for i in range(1,h+1):
    m1=0
    for j in range(n):
        if abs(a[j]-i)>1:
            m1+=abs(a[j]-i)-1
    if m1<m:
        m=m1
        t=i
print(t,m)