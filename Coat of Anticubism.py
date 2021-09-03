# problem name : Coat of Anticubism
# problem link : https://codeforces.com/problemset/problem/667/B
# Rating : 1100

n=int(input())
a=list(map(int, input().split()))
a.sort()
print(abs(a[-1]-sum(a[:n-1]))+1)