for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    if n<=2 or n!=m:
        print(-1)
    else:
        print(2*sum(a))
        for i in range(1,n+1):
            if i==n:
                print(n,1)
            else:
                print(i,i+1)

