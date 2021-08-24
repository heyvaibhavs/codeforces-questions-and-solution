for _ in range(int(input())):
    a,b,c=map(int,input().split())
    n=abs(b-a)*2
    # print("n=",n)
    if n%2!=0 or n<c or a>n or b>n:
        print(-1)
    else:
        if c<=n//2:
            print(n//2+c)
        else:
            print(c-n//2)