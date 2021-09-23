# problem name : Domino Effect
# problem link : https://codeforces.com/problemset/problem/405/B
# Rating : 1100

n=int(input())
s=input()
h=0
c=0
x=''
for i in range(n):
    if s[i]=='.':
        c+=1
    elif len(x)==0 and s[i]=='L':
        c=0
        x='L'
    elif len(x)==0 and s[i]=='R':
        h=c
        c=0
        x='R'
    elif x=='L' and s[i]=='R':
        h+=c
        x='R'
        c=0
    elif x=='R' and s[i]=='L':
        h+=c%2
        x='L'
        c=0
    # print(h,c)
if x=='L' or len(x)==0:
    h+=c
print(h)

     