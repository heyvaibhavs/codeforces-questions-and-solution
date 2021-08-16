# problem name : Feed the cat
# problem link : https://codeforces.com/problemset/problem/955/A
# rating : 1100

h,m=map(int,input().split())
x,d,c,n=map(int,input().split())
if h<20:
    y=60-m+(20-h-1)*60
    if x%n==0:
        z=x//n
    else:
        z=x//n+1
    x+=d*y
    if x%n==0:
        x=x//n
    else:
        x=x//n+1

    print(min(x*c*0.8,z*c))
else:
    if x%n==0:
        x=x//n
    else:
        x=x//n+1
    print(x*c*0.8)