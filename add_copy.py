import math
for i in range(int(input())):
    n=int(input())
    x=2*(math.sqrt(n)-1)
    if x-int(x)==0:
        print(int(x))
    else:
        print(int(x)+1)