for _ in range(int(input())):
    n=int(input())
    i=1
    while n!=0:
        if i%3!=0 and i%10!=3:
            n-=1
        i+=1
    print(i-1)
