# Code by : Sam._.072

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    for i in range(n):
        if a[i]<=i+1+x:
            continue
        else:
            x += a[i]-(i+1+x)
    print(x)