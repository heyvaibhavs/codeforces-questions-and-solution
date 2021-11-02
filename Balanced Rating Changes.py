# Code by : Sam._.072

n=int(input())
a=[]
ans = []
x=0
for i in range(n):
    y = int(input())
    a.append(y)
    ans.append(int(y/2))
    x+=int(y/2)
# print(ans,x)
if x>0:
    for i in range(n):
        if x>0 and a[i]<0 and a[i]%2!=0:
            ans[i] -= 1
            x -= 1
elif x<0:
    x=abs(x)
    for i in range(n):
        if x>0 and a[i]>0 and a[i]%2!=0:
            ans[i] += 1
            x -= 1
for i in ans:
    print(i)
