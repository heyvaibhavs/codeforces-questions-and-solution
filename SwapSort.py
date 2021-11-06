# Code by : Sam._.072

n = int(input())
a = list(map(int, input().split()))
x = sorted(a)
c = 0
ans = []
for i in range(n-1):
    m = i
    for j in range(i+1,n):
        if a[j] < a[m]:
            m = j
    if m != i:
        c += 1
        a[i], a[m] = a[m], a[i]
        ans.append([i,m])      
print(c)
for i in ans:
    print(*i)

