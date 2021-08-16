for _ in range(int(input())):
    n,s,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    if s in a:
        x=a.index(s)
        y=s-1
        for i in range(x-1,-1,-1):
            if a[i]!=y:
                break
            y-=1
        z=s+1
        for i in range(x+1,k,1):
            if a[i]!=z:
                break
            z+=1
        # print(y,z)
        if y<=0:
            print(z-s)
        elif z>=n:
            print(s-y)
        else:
            print(min(s-y,z-s))
    else:
        print(0)

