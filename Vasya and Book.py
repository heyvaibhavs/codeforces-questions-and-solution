import sys , math
for _ in range(int(input())):
    n,x,y,d = map(int, input().split())
    c1=c2=c3=sys.maxsize
    if (y-x)%d==0:
        c1=(y-x)//d
    if (y-1)%d==0:
        c2 = math.ceil((x-1)/d) + (y-1)//d
    if (n-y)%d==0:
        c3 = math.ceil((n-x)/d) + (n-y)//d
    
    z=min(c1,c2,c3)
    if z==sys.maxsize:
        print(-1)
    else:
        print(abs(z))