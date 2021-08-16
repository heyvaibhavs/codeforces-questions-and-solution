n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
f1=5*[0]
f2=5*[0]
for i in range(n):
    f1[a[i]-1]+=1
    f2[b[i]-1]+=1
x,y=0,0
for i in range(5):
    if (f1[i]+f2[i])%2!=0:
        print(-1)
        exit()
    else:
        if f1[i]<(f1[i]+f2[i])//2:
            x+=abs(f1[i]-(f1[i]+f2[i])//2)
        else:
            y+=abs(f2[i]-(f1[i]+f2[i])//2)
if x==y:
    print(x)
else:
    print(-1)

