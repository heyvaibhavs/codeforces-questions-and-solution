for _ in range(int(input())):
    n=int(input())
    l,r=0,10000000000
    for i in range(n):
        x,y=map(int,input().split())
        if x>l:
            l=x
        if y<r:
            r=y
    print(max(0,l-r))
    