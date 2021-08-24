# problem name : Japanese Crosswords Strike Back
# problem link : https://codeforces.com/problemset/problem/884/B
# Rating : 1100

n,x=map(int,input().split())
a=list(map(int,input().split()))
if sum(a)+n-1==x:
    print("YES")
else:
    print("NO")

