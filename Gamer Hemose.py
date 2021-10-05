for _ in range(int(input())):
    n,h=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()
    c=2*(h//(a[-1]+a[-2]))
    h=h%(a[-1]+a[-2])
    if h!=0:
        if h>a[-1]:
            c+=2
        else:
            c+=1
    print(c)