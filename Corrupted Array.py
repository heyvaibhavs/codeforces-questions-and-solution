# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x=sum(a)
    y = x - a[-1]
    z = -1
    for i in range(n+1):
        if y - a[i] == a[-1]:
            a.remove(a[i])
            a.pop()
            z = 1
            break
    if z == -1:
        y = x - a[-2]
        t = a[-2]
        a.remove(a[-2])
        for i in a:
            if y - i == t:
                a.remove(i)
                z = 2
                break
    if z == -1:
        print(-1)
    else:
        print(*a) 

