# Code by : Sam._.072

for _ in range(int(input())):
    x, n = map(int, input().split())
    if n%4==0:
        y=n//4
    else:
        y=n//4+1
    # print(y)
    if n%4==0:
        print(x)
    elif n%4==2:
        if x%2==0:
            print(x+1)
        else:
            print(x-1)
    elif n%4==1:
        if x%2==0:
            print(x-1+(y-1)*(-4))
        else:
            print(x+1+(y-1)*(4))
    elif n%4==3:
        if x%2==0:
            print(x+4+(y-1)*4)
        else:
            print(x-4+(y-1)*(-4)) 