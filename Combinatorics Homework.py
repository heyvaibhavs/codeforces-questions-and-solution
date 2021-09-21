for _ in range(int(input())):
    a,b,c,m=map(int, input().split())
    x=a-1 + b-1 + c-1 
    h=max(a, b,c) 
    y=a+b+c -h
    z=0
    if y < h-1:
        z=h-1-y
    if m>=z and m<=x:
        print("YES")
    else:
        print("NO")


