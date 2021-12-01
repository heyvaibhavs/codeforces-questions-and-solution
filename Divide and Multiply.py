# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    z = sum(a)
    a.sort()
    b = a[:]
    x, y = 0, 0
    for i in range(n-1,-1,-1):
        if a[i]%2!=0 :
            x = a[i]
            a.remove(a[i])
            break
    if x == 0:
        x = a[-1]
        a.remove(a[-1])
    for i in range(n-1,-1,-1):
        if b[i]%2==0 :
            y = b[i]
            b.remove(b[i])
            break
    if y == 0:
        y = b[-1]
        b.remove(b[-1])   
    c1 = 0
    for i in a:
        if i%2!=0:
            c1 += i
        else:
            while i%2 == 0:
                i = i // 2
                x = x * 2
            c1 += i
    c2 = 0
    for i in b:
        if i%2!=0:
            c2 += i
        else:
            while i%2 == 0:
                i = i // 2
                y = y * 2
            c2 += i
    print(max(c1+x,z,c2+y))

    