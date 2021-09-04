# problem name : Home Number
# problem link :https://codeforces.com/problemset/problem/638/A
# Rating : 1100

n,a=map(int, input().split())
if a%2!=0:
    print(a//2+1)
else:
    print(n//2-a//2+1)