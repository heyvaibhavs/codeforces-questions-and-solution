# problem name : Ebony and Ivory
# problem link : https://codeforces.com/problemset/problem/633/A
# Rating : 1100

a,b,c=map(int,input().split())
y,z=1,0
if c%a==0 or c%b==0:
    print("Yes")
    exit()
while c-y*b>0:
    x=(c-y*b)/a
    print(y,x)
    if x-int(x)==0:
        z=-1
        break
    y+=1
if z==-1:
    print("Yes")
else:
    print("No")