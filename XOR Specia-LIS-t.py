# Code by : Sam._.072

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n%2==0:
        print("YES")
    else:
        z=False
        p=-1
        for i in a:
            if i<=p:
                z=True
            p=i

        if z:
            print("YES")
        else:
            print("NO")

