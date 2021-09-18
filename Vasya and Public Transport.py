# problem name : Vasya and Public Transport
# problem link : https://codeforces.com/problemset/problem/355/B
# Rating : 1100

c1,c2,c3,c4 = map(int,input().split())
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# if c4 <= c1 and c4 <= c2 and c4 <= c3:
    # print(c4)
# else:
c=0
for i in range(n):
    if a[i]*c1 < c2:
        c += a[i] * c1
    else:
        c += c2
print(c)
if c3 < c:
    c = c3
x=0
print(c)
for i in range(m):
    if b[i]*c1 < c2 :
        x += b[i] * c1
    else:
        x += c2
print(x)
if c3 < x:
    x = c3
print(x)
print(min(c+x, c4))


