# problem name : Ilya and Diplomas
# problem link : https://codeforces.com/problemset/problem/557/A
# Rating : 1100

n=int(input())
x1,y1=map(int, input().split())
x2,y2=map(int, input().split())
x3,y3=map(int, input().split())
if x1+x2+x3==n:
    print(x1,x2,x3)
elif y1+y2+y3==n:
    print(y1,y2,y3)
else:
    if n-x2-x3>=y1:
        print(y1,end=" ")
        n=n-y1
    else:
        print(n-x2-x3,end=" ")
        n=x2+x3
    # print("n= ",n,end=" ")
    if n-x3>=y2:
        print(y2,end=" ")
        n=n-y2
    else:
        print(n-x3,end=" ")
        n=x3
    print(n)