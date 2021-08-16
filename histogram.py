for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x,y=-1,-1
    for i in range(n):
        if a[i]!=0:
            x=i
            break
    for i in range(n-1,-1,-1):
        if a[i]!=0:
            y=i
            break
    if x==y:
        print(a[x])
    else:
        z=min(a[x],a[y])
        for i in range(x,y+1):
            if a[i]<z:
                z=a[i]
        if z<=min(a[x],a[y]):
            c=2*z
            for i in range(x,y+1):
                c+=a[i]-z
            print(c)
        else:
            z=sum(a)/n
            if z-int(z)==0:
                z=int(z)
            else:
                z=int(z)+1
            c=a[x]+a[y]
            print(c,z)
            for i in range(x+1,y+1):
                if a[i]>a[i-1] and a[i]>=z:
                    c+=a[i]-a[i-1]
                    a[i]=z
                elif a[i]>a[i-1] and a[i]<z:
                    c+=a[i]-a[i-1]
                elif a[i]<a[i-1]:
                    c+=a[i-1]-a[i]
            print(c)
                
