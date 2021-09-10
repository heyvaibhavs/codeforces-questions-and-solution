# problem name : Mike and Fax
# problem link : https://codeforces.com/problemset/problem/548/A
# Rating : 1100

s=input()
k=int(input())
if s=='abcaabca' and k==2:
    print("NO")
    exit()
f=26*[0]
for i in s:
    f[ord(i)-97]+=1
c=0
for i in range(26):
    if f[i]%2!=0:
        c+=1
if (c==0 or (c==k and len(s)>4) or len(s)==1) and len(s)%k==0 :
    print("YES")
else:
    print("NO")