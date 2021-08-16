for _ in range(int(input())):
    a,b,x,y,n=map(int,input().split())
    c1,c2=1000000000000000000,1000000000000000000
    if a-n>=x:
        c1=(a-n)*b
    else:
        n1=n-a+x
        if b-n1>=y:
            c1=x*(b-n1)
        else:
            c1=x*y
    if b-n>=y:
        c2=a*(b-n)
    else:
        n1=n-b+y
        if a-n1>=x:
            c2=y*(a-n1)
        else:
            c2=x*y
    print(min(c1,c2))
        


    


