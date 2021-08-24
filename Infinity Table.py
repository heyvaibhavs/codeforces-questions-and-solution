for _ in range(int(input())):
    k=int(input())
    x=k**0.5
    if x-int(x)==0:
        print(int(x),1)
    else:
        x=int(x)
        if k-x*x<=(x+1):
            print(k-x*x,x+1)
        else:
            x+=1
            print(x,x*x-k+1)
