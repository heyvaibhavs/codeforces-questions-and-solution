# problem name : Email from Polycarp
# problem link : https://codeforces.com/contest/1185/problem/B
# Rating : 1200

for _ in range(int(input())):
    s=input()
    t=input()
    f=26*[0]
    for i in s:
        f[ord(i)-97]+=1
    f1=26*[0]
    for i in t:
        f1[ord(i)-97]+=1
    z=0
    for i in range(26):
        if f[i]>f1[i] or (f[i]==0 and f1[i]!=0) or (f[i]!=0 and f1[i]==0):
            z=-1
            break
    if z==0:
        print("YES")
    else:
        print("NO")

