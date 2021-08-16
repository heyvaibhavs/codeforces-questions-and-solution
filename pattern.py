n=int(input())
def star(n):
    for j in range(n):
        print("*",end="")

def hash(n):
    for j in range(n):
        print("#",end="")
    

k=1
for i in range(1,n+1):
    if i%2!=0:
        star(k)
        hash(n-k)
    else:
        hash(n-k)
        star(k)
    if n%2==0:
        if i<n//2:
            k+=1
        elif i==n//2:
            k=k
        else:
            k-=1
    else:
        if i<=n//2:
            k+=1
        else:
            k-=1
    print()
    # print("k=",k)

