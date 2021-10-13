# Code By : Sam._.072
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    li=[]
    for i in range(1,n):
        if a[i]-a[0]>0:
            li.append(a[i]-a[0])
    if len(li)==0:
        print(-1)
    elif len(li)==1:
        print(li[0])
    else:
        ans=gcd(li[0],li[1])
        for i in range(2,len(li)):
            ans=gcd(ans, li[i])
        print(ans)

