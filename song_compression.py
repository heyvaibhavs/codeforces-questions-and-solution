n,m=map(int, input().split())
d,x,y=[],0,0
for i in range(n):
    x1,y1=map(int, input().split())
    x+=x1
    y+=y1
    d.append(x1-y1)
if y>m:
    print(-1)
else:
    d.sort(reverse=True)
    c=i=0
    while x>m:
        x-=d[i]
        c+=1
        i+=1
    print(c)


