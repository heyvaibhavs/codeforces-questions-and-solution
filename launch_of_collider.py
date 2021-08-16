n=int(input())
s=input()
a=list(map(int,input().split()))
l,z=[],0
for i in range(n-1):
    if (s[i]=='R' and s[i+1]=='L'):
        l.append((a[i+1]-a[i])//2)
        z=-1
if z==0:
    print(-1)
else:
    print(min(l))