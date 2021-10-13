# Code by : Sam._.072

for _ in range(int(input())):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()
    x,c=0,0
    for i in range(k-1,-1,-1):
        if x+n-a[i]<=n:
            c+=1
            x+=n-a[i]
        else:
            break
    ans =c
    p=0
    y=k-c
    for i in range(k-c,k,1):
        if p>=a[i]:
            p+=n-a[y]
            y+=1
            ans-=1
        p+=n-a[i]
    print(ans)