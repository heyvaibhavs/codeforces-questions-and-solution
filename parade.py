# problem name : parade
# problem link : https://codeforces.com/problemset/problem/733/B
# rating : 1100

n=int(input())
l,r=[],[]
ls=rs=0
for i in range(n):
    x,y=map(int, input().split())
    l.append(x)
    r.append(y)
    ls+=x
    rs+=y
x,y=0,abs(ls-rs)
for i in range(n):
    if abs(ls-l[i]+r[i]-rs+r[i]-l[i])>y:
        x=i+1
        y=abs(ls-l[i]+r[i]-rs+r[i]-l[i])
print(x)