# problem name : Quadcopter Competition
# problem link : https://codeforces.com/problemset/problem/883/M
# rating : 1100

x1,y1=map(int, input().split())
x2,y2=map(int, input().split())
if x1==x2:
    print(4+(abs(y1-y2)+1)*2)
elif y1==y2:
    print(4+(abs(x1-x2)+1)*2)
else:
    print((abs(x1-x2)+1)*2+(abs(y1-y2)+1)*2)


