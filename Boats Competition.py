# Code by : Sam._.072

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    d=dict()
    for i in a:
        d[i]=d.get(i,0)+1
    c=0
    for i in range(2,2*n+1):
        t=0
        for j in range(1,i//2+1):
            if j == i-j:
                t += d.get(j,0)//2
            else:
                t += min(d.get(j,0) , d.get(i-j,0))
        if t>c:
            c=t
    print(c)









