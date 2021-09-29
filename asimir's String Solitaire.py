# problem name : asimir's String Solitaire
# problem link : https://codeforces.com/contest/1579/problem/0

for _ in range(int(input())):
    s=input()
    c1,c2,c3=0,0,0
    for i in s:
        if i=='A':
            c1+=1
        elif i=='B':
            c2+=1
        else:
            c3+=1
    if c2==0:
        print("NO")
    elif c2==c1+c3 or (c1==c2 and c3==0) or (c1==0 and c2==c3):
        print("YES")
    else:
        print("NO")





