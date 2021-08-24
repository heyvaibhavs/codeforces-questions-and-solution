a=list(map(int, input().split()))
n=len(a)
x=y=0
for i in range(n):
    if i%2==0:
        x+=a[i]
    else:
        y+=a[i]
es,os=x,y
x1=y1=c=0
for i in range(n):
    if i%2==0:
        x-=a[i]
        es=y+x1
        os=x+y1
        x1+=a[i]
    else:
        y-=a[i]
        es=y+x1
        os=x+y1
        y1+=a[i]
    if os==es:
        c+=1

print(c)
    
    



