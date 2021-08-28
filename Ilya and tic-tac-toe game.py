# problem name : Ilya and tic-tac-toe game
# problem link : https://codeforces.com/problemset/problem/754/B
# Rating : 1100

l=4*[0]
z=0
l[0]=input()
l[1]=input()
l[2]=input()
l[3]=input()
print(l)
for i in range(4):
    for j in range(4):
        if l[i][j]=='x':
            if j+2<4 and l[i][j+1]=='x' and l[i][j+2]=='.':
                z=-1
                break
            elif j-2>=0 and l[i][j-1]=='x' and l[i][j-2]=='x':
                z=-1
                break
            elif i+2<4 and l[i+1][j]=='x' and l[i+2][j]=='x':
                z=-1
                break
            elif i-2>=0 and l[i-1][j]=='x' and l[i-2][j]=='x':
                z=-1
                break
            elif i+2<4 and j+2<4 and l[i+1][j+1]=='x' and l[i+2][j+2]=='x':
                z=-1
                break
            elif i-2>=0 and j-2>=0 and l[i-1][j-1]=='x' and l[i-2][j-2]=='x':
                z=-1
                break
            elif i-2>=0 and j+2<4 and l[i-1][j+1]=='x' and l[i-2][j+2]=='x':
                z=-1
                break
            elif i+2<4 and j-2>=0 and l[i+1][j-1]=='x' and l[i+2][j-2]=='x':
                z=-1
                break
            elif i+1<4 and j+1<4 and i-1>=0 and j-1>=0:
                if l[i+1][j-1]=='x' and l[i-1][j+1]=='x':
                    z=-1
                    break
                elif l[i+1][j+1]=='x' and l[i-1][j-1]=='x':
                    z=-1
                    break
if z==0:
    print("NO")
else:
    print("YES")


