import math
for _ in range(int(input())):
    x=int(input())
    c=0
    while x>=2:
        y=(math.sqrt(1+24*x)-1)//6
        if y>=1:
            c+=1
        else:
            break
        x=x-y*(y+1)-y*(y-1)/2
    print(c)


    