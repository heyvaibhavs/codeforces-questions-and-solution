# Code by : Sam._.072

n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
    a[i] = 3 - a[i]%3
    d[a[i]] = d.get(a[i],0)+1
print(d.get(3,0)//2 + min(d.get(2,0), d.get(1,0)))

    

