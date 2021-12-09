# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    i,j =0, n-1
    while i < j:
        if a[i] != a[j]:
            d[a[i]] = d.get(a[i],0)+1
            d[a[j]] = d.get(a[j],0)+1
        i += 1
        j -= 1 
    if n%2 != 0:
        d[a[n//2]] = d.get(a[n//2],0)+1
        
    if len(d)>2:
        print("NO")
    else:
        print("YES")