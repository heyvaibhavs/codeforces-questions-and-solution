# problem name : Stable Group
# Rating : 1500

n,k,x=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
l=[]
for i in range(n-1):
    if a[i+1]-a[i]>x:
        l.append((a[i+1]-a[i]-1)//x)
l.sort()
c=0
for i in range(len(l)):
    k-=l[i]
    if k>=0:
        c+=1
    else:
        break
print(len(l)-c+1)