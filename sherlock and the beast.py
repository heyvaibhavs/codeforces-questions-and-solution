# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    if n <3 or n == 4  or n==7:
        print(-1)
    elif n%3 == 0:
        print('5'*n)
    else:
        i = 0
        x = 0
        while (n-5*i)>0:
            if (n-5*i)%3==0:
                x = (n-5*i)//3
                break
            i += 1
        x = x*3
        y = i*5
        print('5'*x + '3'*y)
        
