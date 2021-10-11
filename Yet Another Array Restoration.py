for _ in range(int(input())):
    n,x,y=map(int, input().split())
    d=y-x-1
    k = n
    d=y-x
    for i in range(1,(y-x)//2+1):
        # print((y-x+i)%i,(y-x+i)%i==0,(y-x+i)//i<n,(y-x+i)//i)
        if (y-x+i)%i==0 and ((y-x+i)//i)<=n:
            d=i
            break
    i=x
    while k>0 and i<=y:
        print(i,end=" ")
        i+=d
        k-=1
    i=x-d
    while k>0 and i>0:
        print(i,end=" ")
        k-=1
        i=i-d
    i=y+d
    while k>0:
        print(i,end=" ")
        k-=1
        i+=d
        
    print()

