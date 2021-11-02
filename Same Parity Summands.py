# Code by : Sam._.072

for _ in range(int(input())):
    n , k = map(int, input().split())
    if k > n or (n%2 != 0 and k%2 == 0):
        print("NO")
    elif n == k:
        print("YES")
        for i in range(n):
            print(1,end=" ")
        print()
    elif k == 1:
        print("YES")
        print(n)
    elif n%2 !=0 and k%2 !=0:
        print("YES")
        for i in range(k-1):
            print(1,end=" ")
        print(n-k+1)
    elif n%2 ==0 and k > n//2:
        if k%2 != 0:
            print("NO")
        else:
            print("YES")
            for i in range(k-1):
                print(1,end=" ")
            print(n-k+1)
    elif n%2 == 0 and k <= n//2:
        print("YES")
        for i in range(k-1):
            print(2,end=" ")
        print(n-(k-1)*2)
    
