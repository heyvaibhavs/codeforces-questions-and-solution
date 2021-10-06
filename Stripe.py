n=int(input())
a=list(map(int, input().split()))
x=sum(a)
y=0
c=0
for i in range(n-1):
    y+=a[i]
    x-=a[i]
    # print(y,x)
    if x==y:
        c+=1
print(c) 