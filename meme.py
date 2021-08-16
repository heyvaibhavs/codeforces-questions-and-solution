for _ in range(int(input())):
    a,b=map(int,input().split())
    x,k,c=b,0,0
    while x>0:
        if x%10==9:
            k+=1
        c+=1
        x=x//10
    if k==c: 
        print(a*k)
    else:
        print(a*(c-1))