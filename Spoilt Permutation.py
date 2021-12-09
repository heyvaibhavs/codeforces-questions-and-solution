# Code by : Sam._.072

n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
i, j = 0, n-1
while i < n and a[i] == b[i]:
    i += 1
while j >=0 and a[j] == b[j]:
    j -= 1
if i == n or j == -1:
    print(0,0)
else:
    a = a[i:j+1][::-1]
    if a == b[i:j+1]:
        print(i+1,j+1)
    else:
        print(0,0)
