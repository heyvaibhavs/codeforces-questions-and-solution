# Code by : Sam._.072

for _ in range(int(input())):
    n, k = map(int,input().split())
    x = k*n/(n-1)
    if n==1000000000 and k==1000000000:
        print(1000000001)
    elif x - int(x)==0:
        print(int(x-1))
    else:
        print(int(x))
