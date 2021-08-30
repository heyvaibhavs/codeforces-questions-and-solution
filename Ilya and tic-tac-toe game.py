# problem name : Ilya and tic-tac-toe game
# problem link : https://codeforces.com/problemset/problem/754/B
# Rating : 1100

l=4*[0]
z=0
l[0]=input()
l[1]=input()
l[2]=input()
l[3]=input()
def countd(a,b,c,d,e,f,l):
    c1=c2=0
    if l[a][b]=='.':
        c1+=1
    if l[c][d]=='.':
        c1+=1
    if l[e][f]=='.':
        c1+=1
    if l[a][b]=='x':
        c2+=1
    if l[c][d]=='x':
        c2+=1
    if l[e][f]=='x':
        c2+=1
    if c1==1 and c2==2:
        # print(a,b,c,d,e,f)
        return True
    return False

if countd(0,0,0,1,0,2,l):
    z=-1
elif countd(0,1,0,2,0,3,l):
    z=-1
elif countd(0,0,1,0,2,0,l):
    z=-1
elif countd(0,0,1,1,2,2,l):
    z=-1
elif countd(0,1,1,1,2,1,l):
    z=-1
elif countd(0,1,1,2,2,3,l):
    z=-1
elif countd(0,2,1,2,2,2,l):
    z=-1
elif countd(0,3,1,3,2,3,l):
    z=-1
elif countd(1,0,1,1,1,2,l):
    z=-1
elif countd(1,0,2,0,3,0,l):
    z=-1
elif countd(1,0,2,1,3,2,l):
    z=-1
elif countd(1,1,1,2,1,3,l):
    z=-1
elif countd(1,1,2,1,3,1,l):
    z=-1
elif countd(1,1,2,2,3,3,l):
    z=-1
elif countd(1,2,2,2,3,2,l):
    z=-1
elif countd(1,3,2,3,3,3,l):
    z=-1
elif countd(2,0,2,1,2,2,l):
    z=-1
elif countd(2,1,2,2,2,3,l):
    z=-1
elif countd(3,0,3,1,3,2,l):
    z=-1
elif countd(3,1,3,2,3,3,l):
    z=-1
elif countd(2,0,1,1,0,2,l):
    z=-1
elif countd(3,0,2,1,1,2,l):
    z=-1
elif countd(2,1,1,2,0,3,l):
    z=-1
elif countd(3,1,2,2,1,3,l):
    z=-1

if z==0:
    print("NO")
else:
    print("YES")


