for _ in range(int(input())):
    abt=input()
    k,n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    i,j,z,l=0,0,0,[]
    for t in range(n+m):
        if i<n and a[i]==0:
            l.append(0)
            k+=1
            i+=1
        elif j<m and b[j]==0:
            l.append(0)
            k+=1
            j+=1
        elif i<n and a[i]<=k:
            l.append(a[i])
            i+=1
        elif j <m and b[j]<=k:
            l.append(b[j])
            j+=1
        else:
            z=-1
            break
    if z==-1:
        print(-1)
    else:
        print(*l)

    
        

    





