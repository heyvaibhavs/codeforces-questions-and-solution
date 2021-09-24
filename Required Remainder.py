# problem name : Required Remainder

for _ in range(int(input())):
    x,y,n=map(int, input().split())
    z=(n//x)*x
    if z+y<=n:
        z=z+y
    else:
        z=((n//x)-1)*x+y
    print(z)