# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    x = (2 * sum(a))/n
    if x - int(x) != 0:
        print(0)
    else:
        x = int(x)
        d = dict()
        for i in a:
            d[i] = d.get(i,0)+1
        c = 0
        for i in a:
            if d.get(x-i,0)>0:
                if x%2==0 and x//2 == i:
                    c += (d[x-i]-1)*d[x-i]//2
                    d[i] = 0
                    d[x-i] = 0
                else:
                    c += d[i]*d[x-i]
                    d[i] = 0
                    d[x-i] = 0
                
        print(c)



