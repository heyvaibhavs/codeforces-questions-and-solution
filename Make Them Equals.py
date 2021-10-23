# Code by : Sam._.072

n=int(input())
a=list(map(int, input().split()))
if len(set(a))==1:
    print(0)
    exit()
z=[]
for i in range(1,101):
    x=[]
    for j in a:
        if i!=j:
            x.append(abs(j-i))
    x=list(set(x))
    if len(x)==1:
        z.append(x[0])
if len(z)==0:
    print(-1)
else:
    z.sort()
    print(z[0])
    