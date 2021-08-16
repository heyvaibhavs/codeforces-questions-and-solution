for _ in range(int(input())):
    x1,y1,z1=map(int,input().split())
    x2,y2,z2=map(int,input().split())
    t=min(y1,x2)
    y1-=t
    x2-=t
    t=min(x1,z2)
    x1-=t
    z2-=t
    c=2*min(z1,y2) - 2*min(y1,z2)
    print(c)




