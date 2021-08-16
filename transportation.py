n,k=map(int,input().split())
a=list(map(int,input().split()))
l,i=[],1
while i <=n-1:
    i+=a[i-1]
    if i==k:
        print("YES")
        exit()

print("NO")

