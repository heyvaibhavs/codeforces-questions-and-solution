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
        x=[]
        for i in d:
            t=d[i]
            while t>1:
                x.append(i)
                t=t//2
        x.sort()
        t=x[0]*x[-1]
        z=0
        for i in range(1,n):
            if x[i]*x[2*n-1-i]!=t:
                z=-1
                break
        if z==0:
            print("YES")
        else:
            print("NO")
