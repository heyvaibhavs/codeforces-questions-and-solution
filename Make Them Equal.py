# Code by : Sam._.072

for _ in range(int(input())):
    t = list(input().split())
    s = input()
    n, x = int(t[0]), t[1]
    # print(s[1::2],s[::2])
    if len(set(s)) == 1 and s[0] == x:
        print(0)
    else:
        z = -1
        for i in range(n-1,-1,-1):
            if s[i]==x:
                z=i+1
                break
        if z == -1:
            print(2)
            print(n-1,n)
        elif z*2>n:
            print(1)
            print(z)
        else:
            print(2)
            print(n-1,n)