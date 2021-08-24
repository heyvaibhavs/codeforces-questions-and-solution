def minc(l,r):
    if r-l==2:
        return 2
    elif r-l==3:
        return 5
    return (r-l)+minc(l, l+(r-l)//2)+minc(l+(r-l)//2, r)

for _ in range(int(input())):
    n,m=map(int,input().split())
    x=(n+1)*(n+2)//2 -1
    y=minc(0,n+1)
    if m>=y:
        if m>=y and m<=x:
            print(min(x-m,m-y))
        else:
            print(m-x)
    else:
        print(-1)




