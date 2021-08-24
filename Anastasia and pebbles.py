# problem name : Anastasia and pebbles
# problem link : https://codeforces.com/problemset/problem/789/A
# rating : 1100

import math
n,k=map(int,input().split())
a=list(map(int, input().split()))
c=c1=0
for i in range(n):
    c+=int(a[i]//(2*k))
    a[i]=a[i]%(2*k)
    if a[i]>k:
        c+=1
        a[i]=0
    if a[i]>0:
        c1+=1
# print(a)

print(c+math.ceil(c1/2))