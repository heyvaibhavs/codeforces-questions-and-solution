# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0]==n:
        a = a[1:]
        print(n,*a[::-1])
    elif a[-1]==n:
        a.pop()
        print(*a[::-1],n)
    else:
        print(-1)
        
    
