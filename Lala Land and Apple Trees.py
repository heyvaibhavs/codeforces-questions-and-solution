# problem name : Lala Land and Apple Trees
# problem link : https://codeforces.com/problemset/problem/558/A
# Rating : 1100

n=int(input())
d=dict()
c1=c2=0
l1,l2=[],[]
for i in range(n):
    x,y=map(int, input().split())
    d[x]=y
    if x<0:
        c1+=1
        l1.append(x)
    else:
        c2+=1
        l2.append(x)
l1.sort()
l2.sort()
c=0
# print(l1,l2)
if c1>c2:
    for i in range(c2):
        c+=d[l2[i]]
    for i in range(c1-c2-1,c1):
        c+=d[l1[i]]
    print(c)
elif c1<c2:
    for i in range(c1):
        c+=d[l1[i]]
    for i in range(c1+1):
        c+=d[l2[i]]
    print(c)
else:
    for i in range(c1):
        c+=d[l1[i]]+d[l2[i]]
    print(c)





