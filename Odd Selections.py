# Code by : Sam._.072

for _ in range(int(input())):
    n,x = map(int, input().split())
    a=list(map(int, input().split()))
    c1,c2=0,0
    for i in a:
        if i%2==0:
            c1+=1
        else:
            c2+=1
    if c2==0:
        print("NO")
    elif c1==0:
        if (n==x and n%2==0):
            print("NO")
        elif x%2==0:
            print("NO")
        else:
            print("YES")
    elif x==n:
        if sum(a)%2!=0:
            print("YES")
        else:
            print("NO")
    elif c2>=1:
        print("YES")
    else:
        print("NO")
        
    