# problem name : The number on the board
# problem link : https://codeforces.com/problemset/problem/835/B
# rating : 1100

k=int(input())
n=input()
c=0
for i in n:
    c+=int(i)
if c>=k:
    print(0)
else:
    n=sorted(n)
    c1=0
    for i in n:
        c+=(9-int(i))
        c1+=1
        if c>=k:
            break
    print(c1)