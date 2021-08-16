for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x,y,x1,y1=[],[],0,0
    for i in range(n):
        if i%2==0:
            x.append(a[i])
            x1+=a[i]
        else:
            y.append(a[i])
            y1+=a[i]
    if x1==y1:
        print(n)
        print(*a)
    else:
        x1,y1=0,0
        for i in range(n//2):
            
            if i%2==0:
                x1+=x[i]
            else:
                y1+=x[i]
        if x1==y1:
            print(len(x))
            print(*x)
        else:
            print(len(y))
            print(*y)


