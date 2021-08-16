for _ in range(int(input())):
    n,d=map(int,input().split())
    if n%2==0:
        if d%(n//2+1)==0:
            x=d//(n//2+1)
        else:
            x=d//(n//2+1)+1
        if n//2+x<=n:
            print("YES")
        else:
            print("NO")
    else:
        if d%(n//2+1)==0:
            x=d//(n//2+1)
        else:
            x=d//(n//2+1)+1
        if d%(n//2+2)==0:
            y=d//(n//2+2)
        else:
            y=d//(n//2+2)+1
        if n//2+x<=n or n//2+1+y<=n:
            print("YES")
        else:
            print("NO")
    