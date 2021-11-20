# Code by : Sam._.072

n = int(input())
a = list(map(int, input().split()))
a1 = a[:]
c, x = 0, 0
b = sorted(a)
while a!=b and c <= 2*n:
    if x == 0:
        for i in range(0,2*n,2):
            a[i], a[i+1] = a[i+1], a[i]
        c += 1
        x = 1
    else:
        for i in range(n):
            a[i], a[n+i] = a[n+i], a[i]
        c += 1
        x = 0
    # print("c : ",c,x)
c1, x = 0, 0
while a1 != b and c1 <= 2*n:
    if x == 0:
        for i in range(n):
            a1[i], a1[n+i] = a1[n+i], a1[i]
        c1 += 1
        x = 1
    else:
        for i in range(0,2*n,2):
            a1[i], a1[i+1] = a1[i+1], a1[i]
        c1 += 1
        x = 0
    # print("c1 : ",c1,x)
# print(c,c1)
if min(c, c1) < 2*n:
    print(min(c, c1))
else:
    print(-1)

 

