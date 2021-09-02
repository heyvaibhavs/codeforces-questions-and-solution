# problem name : Infinite sequence
# problem link : https://codeforces.com/problemset/problem/675/A
# Rating : 1100

a,b,c=map(int, input().split())
if c==0:
    if a==b:
        print("YES")
    else:
        print("NO")
else:
    n= (b-a)/c + 1
    if (b-a)/c<0:
        print("NO")
    elif n - int(n)==0:
        print("YES")
    else:
        print("NO")
