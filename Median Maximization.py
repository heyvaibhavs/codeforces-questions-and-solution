# problem name : Median Maximization
# problem link : https://codeforces.com/contest/1566/problem/A

for i in range(int(input())):
    n,m=map(int,input().split())
    c=n//2
    if n%2!=0:
        c+=1
    n=n-c+1
    print(m//n)