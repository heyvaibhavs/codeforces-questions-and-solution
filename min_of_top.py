l1=list(map(int,input().split()))
# l1.reverse()
l,x=[],0
for i in l1:
    if len(l)==0:
        l.append(i)
        x=i
    elif i<x:
        l.append(i)
        x=i
    else:
        l.append(x)
l.reverse()
print(l)  