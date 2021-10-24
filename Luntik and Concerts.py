for _ in range(int(input())):
    a,b,c=map(int, input().split())
    if (a+2*b+3*c)%2==0:
        print(0)
    else:
        print(1)