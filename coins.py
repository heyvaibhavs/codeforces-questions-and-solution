for _ in range(int(input())):
    n=int(input())
    x=n/3
    if x-int(x)==0:
        print(int(x),int(x))
    elif int(x)+2*(int(x)+1)==n:
        print(int(x),int(x)+1)
    else:
        print(int(x)+1,int(x))