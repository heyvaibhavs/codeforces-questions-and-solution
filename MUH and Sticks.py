# problem name : MUH and Sticks
# problem link : https://codeforces.com/problemset/problem/471/A
# Rating : 1100

a=list(map(int,input().split()))
d=dict()
for i in a:
    d[i]=d.get(i,0)+1
z=0
if len(d)<=3:
    l=list(d.values())
    l.sort()
    if len(d)==2:
        if l[0]==1:
            z=1
        elif l[0]==2:
            z=2
    elif len(l)==3:
        if l[0]==1 and l[1]==1 and l[2]==4:
            z=1
    else:
        z=2
if z==1:
    print("Bear")
elif z==2:
    print("Elephant")
else:
    print("Alien")

