for _ in range(int(input())):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    f=n*[0]
    for i in s:
        f[i-1]+=1
    x,y,z=0,0,0
    for i in range(n):
        if f[i]>=k:
            x+=1
        elif f[i]==1:
            y+=1
        elif f[i]==2:
            z+=1
    c=x+(y+2*z)//k
    print(c)