for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==0 or b==0:
        print(0)
    elif a==b or abs(a-b)==1 or abs(a-b)==2:
        print((a+b)//3)
    elif b>=2*a:
        print(a)
    elif a>=2*b:
        print(b)
    elif min(a,b)>=(a+b)//3:
        print((a+b)//3)
    else:
        print(min(a,b))
