import math
n=int(input())
a=(n+1)*[True]
a[0],a[1]=False,False
x=int(math.sqrt(n))
for i in range(2,x+1):
    if a[i]==True:
        j=i*i
        while j<=n:
            # print(j,end=" ")
            if j%i==0:
                a[j]=False
            j+=i
# print(a)
print(a.count(True))

