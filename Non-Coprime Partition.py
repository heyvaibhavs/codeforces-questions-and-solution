n=int(input())
if n==1 or n==2:
    print("NO")
else:
    print("YES")
    k=n*(n+1)//2
    for i in range(2,n+1):
        if (k-i)%i==0:
            print(1,i)
            print(n-1,end=" ")
            for j in range(1,n+1):
                if j!=i:
                    print(j,end=" ")
            break