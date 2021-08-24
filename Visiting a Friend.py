# problem name: Visiting a Friend
# problem link : https://codeforces.com/problemset/problem/902/A
# problem rating : 1100

n,m=map(int,input().split())
x=y=0
for i in range(n):
    a,b=map(int,input().split())
    if a<=x and y==0:
        if b>x:
            x=b
    else:
        y=-1
if y==0 and x==m:
    print("YES")
else:
    print("NO")