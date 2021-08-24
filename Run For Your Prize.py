n=int(input())
a=list(map(int,input().split()))
c=10000000
for i in range(n-1):
    c=min(max(a[i]-1,1000000-a[i+1]),c)
print(min(a[-1]-1,1000000-a[0],c))
    


