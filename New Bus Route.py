# problem Name : New Bus Route
# problem link : https://codeforces.com/problemset/problem/792/A
# rating : 1100

n=int(input())
a=list(map(int, input().split()))
a.sort()
h=a[1]-a[0]
for i in range(n-1):
    a[i]=a[i+1]-a[i]
    if h>a[i]:
        h=a[i]
a.pop()
print(h,a.count(h))

