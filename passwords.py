# problem name : passwords
# problem link : https://codeforces.com/problemset/problem/721/B
# rating : 1100

n,k=map(int,input().split())
l,s=[],[]
for i in range(n+1):
    s1=input()
    if i==0:
        s.append(s1)
        l.append(len(s1))
    elif i>0 and  s[-1]!=s1:
        l.append(len(s1))
        s.append(s1)
n=len(s)-1

if len(s)==1:
    print(1,1)
elif len(set(l))==1:
    print(1,(n//k)*5+n)
else:
    for i in range(len(l)-1,0,-1):
        if l[i]==l[i-1]:
            print(i,(n//k)*5+n)
            break