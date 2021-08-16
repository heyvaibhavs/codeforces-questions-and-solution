n=int(input())
l,b,c,ans=n*[0],n*[0],0,[]
# print(l,b)
for i in range(1,n*n+1):
    x,y=map(int,input().split())
    if l[x-1]==0 and b[y-1]==0:
        ans.append(i)
        l[x-1]=1 
        b[y-1]=1
print(*ans)