# Code by : Sam._.072
import sys
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x=a[0]
    h=a[0]
    for i in range(1,n):
        if a[i]-x>h:
            h=a[i]-x
        x+=(a[i]-x)
    print(h)
