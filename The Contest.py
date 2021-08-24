# problem name : The contest
# problem link : https://codeforces.com/problemset/problem/813/A
# rating : 1100

n=int(input())
a=list(map(int, input().split()))
m=int(input())
y=[]
x=[]
for i in range(m):
    x1,y1=map(int, input().split())
    x.append(x1)
    y.append(y1)
if m==0 or sum(a)>y[-1]:
    print(-1)
else:
    i=j=p=c=0
    # print(x,y)
    while i<n:
        p+=a[i]
        while j<m:
            if p>=x[j] and p<=y[j]:
                c=p
                break
            elif p<x[j]:
                c=x[j]
                break
            elif p>y[j]:
                j+=1
        i+=1
    
    print(c)
