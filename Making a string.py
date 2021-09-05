# problem name : Making a string
# problem link : https://codeforces.com/problemset/problem/624/B
# Rating : 1100

n=int(input())
a=list(map(int, input().split()))
a.sort(reverse=True)
c=x=y=a[0]
for i in range(1,n):
    if a[i]<x:
        c+=a[i]
        x=a[i]
    else:
        x-=1
        c+=x
    if x==0:
        break
print(c)

