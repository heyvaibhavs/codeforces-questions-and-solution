# problem name : Rook, Bishop and King
# problem link : https://codeforces.com/problemset/problem/370/A
# Rating : 1100

r1,c1,r2,c2 = map(int, input().split())
if r1==r2 or c1==c2:
    x=1
else:
    x=2
if (r1+c1)%2 != (r2+c2)%2:
    y=0
else:
    if r1+c1==r2+c2 or r1-c1 == r2-c2:
        y=1
    else:
        y=2
z=max(abs(r2-r1), abs(c2-c1))
print(x,y,z)
