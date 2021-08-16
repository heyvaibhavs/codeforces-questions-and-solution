for _ in range(int(input())):
    z=input()
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    if x1==x2:
        if x3==x1 and y3>min(y1,y2) and y3<max(y1,y2):
            print(abs(y1-y2)+2)
        else:
            print(abs(y1-y2))
    elif y1==y2:
        if y3==y1 and x3>min(x1,x2) and x3<max(x1,x2):
            print(abs(x1-x2)+2)
        else:
            print(abs(x1-x2))
    else:
        print(abs(x1-x2)+abs(y1-y2))