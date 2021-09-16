# problem name : Fixed points
# problem link : https://codeforces.com/problemset/problem/347/B
# Rating : 1100

n=int(input())
a=list(map(int, input().split()))
d=dict()
c=0
for i in range(n):
    if i==a[i]:
        c+=1
    else:
        d[i]=a[i]
for i in d:
    if d[d[i]]==i:
        print(c+2)
        exit(0)
if c==n:
    print(c)
else:
    print(c+1)



