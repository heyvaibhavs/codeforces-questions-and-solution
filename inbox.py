n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n-1):
    if a[i]==1 and a[i+1]==1:
        c+=1
    elif a[i]==1 and a[i+1]==0:
        c+=2
if a[n-1]==1:
    c+=1
elif a[n-1]==0 and c>0:
    c-=1
print(c)
