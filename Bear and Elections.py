n=int(input())
a=list(map(int,input().split()))
k=a[0]
a=a[1:]
a.sort()
c=0
while k<=a[-1]:
    k+=1
    a[-1]-=1
    a.sort()
    c+=1
    # print(a,k)
print(c)


