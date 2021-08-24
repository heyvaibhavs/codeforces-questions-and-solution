# problem name : Vicious keyboard
# problem link : https://codeforces.com/problemset/problem/801/A
# rating : 1100

s=input()
c=z=i=0
if s=='VV' or s=='KK':
    print(1)
    exit(0)
n=len(s)
while i<n-1:
    if s[i]=='V' and s[i+1]=='K':
        c+=1
        i+=1
    elif  i+2<n and s[i]=='V' and s[i+1]=='V' and z==0 and s[i+2]=='V':
        z=-1
        i+=1
    elif s[i]=='K' and s[i+1]=='K' and z==0:
        z=-1
        i+=1
    i+=1
# print(c,z)
if s[-1]=='V' and s[-2]=='V':
    z=-1
if z==-1:
    print(c+1)
else:
    print(c)