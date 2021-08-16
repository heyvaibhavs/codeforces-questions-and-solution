for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    c=x=y=0
    for i in range(n):
        a[i]=a[i]%3
        if a[i]==0:
            c+=1
        elif a[i]==1:
            x+=1
        else:
            y+=1
    t=min(x,y)
    x-=t
    y-=t
    print(c+t+x//3+y//3)