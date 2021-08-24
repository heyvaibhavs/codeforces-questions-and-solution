# problem name : The Festive Evening
# problem link : https://codeforces.com/problemset/problem/834/B
#  rating : 1100

n,k=map(int,input().split())
s=input()
f=26*[0]
for i in s:
    f[ord(i)-65]+=1
a=f[:]
c=0
for i in s:
    if f[ord(i)-65]==a[ord(i)-65]:
        c+=1
    a[ord(i)-65]-=1
   
    # print(c)
    if c>k:
        print("YES")
        exit(0)
    if a[ord(i)-65]==0:
        c-=1
print("NO")
