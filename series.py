import sys
n, s = map(int, input().split())
a = list(map(int, input().split()))
i, c= 0,0
x, y = sys.maxsize , 0
while i < n:
    if a[i] < x:
        x = a[i]
    if a[i] > y:
        y = a[i]
    if y - x > s:
        x , y= a[i], a[i]
        c += 1
    i += 1
     
print(c+1)
