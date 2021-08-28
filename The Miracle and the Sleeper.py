for _ in range(int(input())):
    l,r=map(int,input().split())

    if l==r:
        print(0)
    else:
            
        if r//l==1:
            print(r%l)
        else:
            print(int(r%(r//2+1)))

