for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    p,k,l=n,n,(n+1)*[0]
    for i in range(n-1,0,-1):
        if a[i]==p:
            l[a[i]]=1
            print(*a[i:k],end=" ")
            for j in range(p-1,-1,-1):
                if l[j]==0:
                    p=j
                    break
            k=i
            # print(p,k)
        else:
            l[a[i]]=1
        # print(l)
    print(*a[:k],end=" ")
    print()
        



