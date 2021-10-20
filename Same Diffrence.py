# Code by : Sam._.072

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    for i in range(n):
        a[i]=a[i]-i-1
    d=dict()
    for i in range(n):
        d[a[i]]=d.get(a[i],0)+1
    c=0
    for i in d:
        c+= d[i]*(d[i]-1)//2
    print(c)