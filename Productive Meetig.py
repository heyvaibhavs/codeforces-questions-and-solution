# problem name : Productive Meeting
# problem link : https://codeforces.com/contest/1579/problem/D

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    d=dict()
    for i in range(n):
        d[i+1]=a[i]
    d=dict(sorted(d.items(),key=lambda x: x[1]))
    
