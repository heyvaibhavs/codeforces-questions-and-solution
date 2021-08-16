for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    h=0
    for i in range(n-1):
        if a[i]*a[i+1]>h:
            h=a[i]*a[i+1]
    print(h)
        
