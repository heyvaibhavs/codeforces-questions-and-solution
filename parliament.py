n,a,b=map(int,input().split())
if n>a*b:
    print(-1)
elif b%2!=0:
    t=1
    for i in range(a):
        for j in range(b):
            if t<=n:
                print(t,end=" ")
                t+=1
            else:
                print(0,end=" ")
        print()
else:
    t,l=1,[]
    for i in range(a):
        for j in range(b):
            if t <=n:
                print(t,end=" ")
                t+=1
            else:
                if len(l)>0:
                    for i in range(len(l)):

        if t<=n:
            l.append(t)
            t+=1
        print()
    print(l)