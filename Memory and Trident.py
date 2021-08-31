# problem name : Memory and Trident
# problem link : https://codeforces.com/problemset/problem/712/B
# rating : 1100

s=input()
x,y=0,0
for i in s:
    if i=='L':
        x+=1
    elif i=='R':
        x-=1
    elif i=='U':
        y+=1
    else:
        y-=1
if (abs(x)+abs(y))%2!=0:
    print(-1)
else:
    print((abs(x)+abs(y))//2)