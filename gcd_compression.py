for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x,y=[],[]
    for i in range(0,2*n):
        if a[i]%2==0:
            x.append(i+1)
        else:
            y.append(i+1)
    if len(x)%2!=0:
        x.pop()
    if len(y)%2!=0:
        y.pop()
    c=0
    for i in range(0,len(x),2):
        if c<n-1:
            print(x[i],x[i+1])
            c+=1
    for i in range(0,len(y),2):
        if c<n-1:
            print(y[i],y[i+1])
            c+=1
    
