n,k=map(int, input().split())
i=1
while True:
    if (i*(10**k))%n==0:
        print(i*(10**k))
        break
    i+=1



