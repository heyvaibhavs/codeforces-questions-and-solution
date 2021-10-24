for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    c0,c1=0,0
    s=0
    for i in a:
        if i==0:
            c0+=1
        elif i==1:
            c1+=1
        s+=i
    if s==1:
        print(2**c0)
    elif c0==0:
        print(c1)
    elif c1==0:
        print(0)
    else:
        print(c1*(2**c0))