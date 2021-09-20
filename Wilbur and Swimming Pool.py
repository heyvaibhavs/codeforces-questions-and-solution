# problem name : Wilbur and Swimming Pool
# problem link : https://codeforces.com/problemset/problem/596/A
# Rating : 1100

n=int(input())
x=set()
y=set()
for i in range(n):
    x1,y1 = map(int, input().split())
    x.add(x1)
    y.add(y1)
if n==1 or len(x)==1 or len(y)==1:
    print(-1)
else:
    x=list(x)
    y=list(y)
    print(abs(x[1]-x[0])*abs(y[1]-y[0]))