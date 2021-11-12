# Code by : Sam._.072

for _ in range(int(input())):
    a1,a2,a3=map(int, input().split())
    if a1+a3-2*a2==0:
        print(0)
    elif (a1+a3-2*a2)%3==0:
        print(0)
    else:
        print(1)