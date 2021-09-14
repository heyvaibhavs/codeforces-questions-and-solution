# problem name : Misha and Changing Handles
# problem link : https://codeforces.com/problemset/problem/501/B
# Rating : 1100

def getParent(d,p):
    if d.get(d[p],-1)==-1:
        return d[p]
    return getParent(d, d[p])

n=int(input())
d=dict()
for i in range(n):
    x,y=map(str, input().split())
    d[x]=y
d1=dict()
c=0
for i in d:
    x=getParent(d, i)
    if d1.get(x,-1)==-1:
        d1[x]=i
        c+=1    
del d
print(c)
for i in d1:
    print(d1[i],i)