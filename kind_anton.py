for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if a[0]!=b[0]:
        print("NO")
    elif a==b:
        print("YES")
    else:
        f=3*[0]
        z=0
        for i in range(n):
            f[a[i]]+=1
        # print(f)
        for i in range(n-1,0,-1):
            f[a[i]]-=1
            if a[i]!=b[i]:
                if b[i]>a[i] and f[1]>0:
                    continue
                elif b[i]<a[i] and f[-1]>0:
                    continue
                else:
                    z=-1
                    break
            # print(f)
        if z==-1:
            print("NO")
        else:
            print("YES")
                
