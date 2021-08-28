# problem name : Blown Garland
# problem link : https://codeforces.com/problemset/problem/758/B
# rating : 1100

s=input()
l=4*["x"]
n,i,x=len(s),0,4
while i <n:
    if l[i%4]=='x' and s[i]!='!':
        l[i%4]=s[i]
        x-=1
    if x<=0:
        break
    i+=1
f,i=4*[0],0
while i<n:
    if l[i%4]!=s[i]:
        f[i%4]+=1
    i+=1
print(f[l.index('R')],f[l.index('B')],f[l.index('Y')],f[l.index('G')])


