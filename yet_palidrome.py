for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    f=(n+1)*[0]
    x=(n+1)*[-1]
    z=0
    for i in range(n):
        f[a[i]]+=1
        if f[a[i]]==3:
            z=-1
            break
        if x[a[i]]==-1:
            x[a[i]]=i
        elif i-x[a[i]]==1:
            x[a[i]]=i
        else:
            z=-1
            break
    if z==-1:
        print("YES")
    else:
        print("NO")
        


