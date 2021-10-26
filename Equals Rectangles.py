# Code by : Sam._.072

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    d=dict()
    for i in a:
        d[i]=d.get(i,0)+1
    z=0
    for i in d:
        if d[i]%2!=0:
            z=-1
            break
    if z==-1:
        print("NO")
    else:
        a.sort()
        t=a[0]*a[-1]
        z=0
        for i in range(1,n*2):
            if a[i]*a[4*n-1-i]!=t:
                z=-1
                break
        if z==0:
            print("YES")
        else:
            print("NO")
