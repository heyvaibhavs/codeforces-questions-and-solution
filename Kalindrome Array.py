# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for i in a:
        d[i] = d.get(i,0)+1
    c = 0
    for i in d:
        if d[i]==1:
            c+=1
    if n <= 2:
        print("YES")
    elif c>2:
        print("NO")
    elif c == 2:
        if d[a[0]]==1 and d[a[-1]]==1:
            print("NO")
        else:
            z = 0
            for i in range(n-1):
                if d[a[i]]==1 and d[a[i+1]]==1:
                    z = -1
                    break
            if z == -1:
                print("NO")
            else:
                print("YES")
    else:
        print("YES") 