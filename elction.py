for _ in range(int(input())):
    a,b,c=map(int, input().split())
    h=max(a, b, c)
    if a==b==c:
        print(1,1,1)
    else:
        l=[a,b,c]
        l.sort()
        if l[-1]==l[-2] and l[-2]==h:
            if a==h:
                print(1,end=" ")
            else:
                print(h-a+1,end=" ")
            if b==h:
                print(1,end=" ")
            else:
                print(h-b+1,end=" ")
            if c==h:
                print(1,end=" ")
            else:
                print(h-c+1,end=' ')
        else:
            if a==h:
                print(0,end=" ")
            else:
                print(h-a+1,end=" ")
            if b==h:
                print(0,end=" ")
            else:
                print(h-b+1,end=" ")
            if h==c:
                print(0,end=" ")
            else:
                print(h-c+1,end=" ")
        print()