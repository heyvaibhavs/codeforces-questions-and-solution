for _ in range(int(input())):
    n,x=map(int, input().split())
    a=list(map(int, input().split()))
    b=sorted(a)
    if b==a or x<=n//2:
        print("YES")
    elif x>=n:
        print("NO")
    else:
    
        z=0
        for i in range(n-x,x):
            if a[i]!=b[i]:
                z=-1
                break
        if z==0:
            print("YES")
        else:
            print("NO")
    
