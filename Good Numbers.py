# problem name : Good Numbers
# problem link : https://codeforces.com/problemset/problem/365/A
# rating : 1100

def countK(s,k):
    f=10*[0]
    for i in s:
        f[ord(i)-48]+=1
    # print(f)
    for i in range(k+1):
        if f[i]==0:
            return False
    return True
    
n,k=map(int, input().split())
c=0
for i in range(n):
    a=input()
    if countK(a, k):
        c+=1

print(c) 

