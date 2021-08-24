# problem name : Carrot Cake
# problem link : https://codeforces.com/problemset/problem/799/A
# Rating : 1100
import math
n,t,k,d=map(int,input().split())
x=math.ceil(n/k)*t
y,i=0,1
while n>0:
    if i%t==0:
        y=i
        n-=k
        # print(y,n)
    if (i-d)>0 and (i-d)%t==0 and i!=d:
        y=i
        n-=k
        # print(y,n)
    i+=1
if y<x:
    print("YES")
else:
    print("NO")