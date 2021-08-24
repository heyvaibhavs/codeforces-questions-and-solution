# problem name : chess tourney
# problem link : https://codeforces.com/problemset/problem/845/A
# rating : 1100

n=int(input())
a=list(map(int, input().split()))
a.sort()
# print(a[n//2],a[n//2-1],(n//2)-1)
if a[n]>a[n-1]:
    print("YES")
else:
    print("NO")