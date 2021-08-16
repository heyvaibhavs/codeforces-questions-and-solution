n=int(input())
a=list(map(int,input().split()))
a.sort()
t=a[-2]
a[-2]=a[-1]
a[-1]=t
if a[-2]+a[0]>a[-1]:
    z=0
    for i in range(n-2):
        if a[i]+a[i+2]<=a[i+1]:
            z=-1
            break
    if z==0:
        print("YES")
        print(*a)
    else:
        print("NO")
else:
    print("NO")
