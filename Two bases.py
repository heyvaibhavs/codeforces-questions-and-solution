# problem Name : Two bases
# problem link : https://codeforces.com/problemset/problem/602/A
# Rating : 1100

n,b1=map(int, input().split())
l1=list(map(int, input().split()))
m,b2=map(int, input().split())
l2=list(map(int, input().split()))
x=y=0
p=1
for i in range(n-1,-1,-1):
    x+=l1[i]*p
    p=p*b1
p=1
for i in range(m-1,-1,-1):
    y+=l2[i]*p
    p=p*b2
if x==y:
    print("=")
elif x<y:
    print("<")
else:
    print(">")
