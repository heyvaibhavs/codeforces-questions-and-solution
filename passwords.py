# problem name : passwords
# problem link : https://codeforces.com/problemset/problem/721/B
# rating : 1100

n,k=map(int,input().split())
l=[]
for i in range(n):
    s=input()
    l.append(len(s))
s=input()
if n==1:
    print(1,1)
    exit()
l.sort()
h1=l.index(len(s))
h2=-1
for i in range(h1+1,n):
    if l[i]>len(s):
        h2=i-1
        break
# print(h2)
if h2==-1:
    h2=n-1
# print(h1,h2)
h1=h1+1+(h1//k)*5
h2=h2+1+(h2//k)*5   
print(h1,h2)
