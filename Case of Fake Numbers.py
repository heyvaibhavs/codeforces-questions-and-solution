# problem name : Case of Fake Numbers
# problem link : https://codeforces.com/problemset/problem/556/B
# rating : 1100

n=int(input())
a=list(map(int, input().split()))
l=[i for i in range(n)]
if l==a:
    print("YES")
    exit()
for i in range(n):
    if i%2==0:
        if i==0:
            a[i]=n-a[i]
        elif i>=a[i]:
            a[i]=i-a[i]
        else:
            a[i]=n-a[i]+i
    else:
        if i<=a[i]:
            a[i]=a[i]-i
        else:
            a[i]=a[i]+n-i

if a.count(a[0])==n:
    print("YES")
else:
    print("NO")



