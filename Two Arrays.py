# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    z=0
    for i in range(n):
        if b[i]-a[i]!=1 and a[i]!=b[i]:
            z=-1
            break
    if z==0:
        print("YES")
    else:
        print("NO")