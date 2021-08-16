n=int(input())
m=int(input())
a,k,h=[],0,0
m1=m
# print(n)
for i in range(n):
    t=int(input())
    a.append(t)
    if t>h:
        h=t
a.sort()
for i in range(n):
    if a[i]<h and m>0:
        m=m-(h-a[i])
        a[i]=h
        k+=a[i]
    else:
        k+=a[i]
if m<0:
    print(h,h+m1)
else:
    if (k+m)%n==0:
        k=(m+k)//n
    else:
        k=(k+m)//n+1

    print(k,h+m1)


