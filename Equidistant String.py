# problem name : Equidistant String
# problem link : https://codeforces.com/problemset/problem/545/B
# Rating : 1100

s=input()
t=input()
c,n=0,len(s)
for i in range(n):
    if s[i]!=t[i]:
        c+=1
if c%2==0:
    p=''
    x=0
    for i in range(n):
        if s[i]==t[i]:
            p += s[i]
        elif x==0:
            p += s[i]
            x=-1
        else:
            p += t[i]
            x=0
    print(p)
else:
    print("impossible")