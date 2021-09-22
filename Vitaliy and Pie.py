# problem name : Vitaliy and Pie
# problem link : https://codeforces.com/problemset/problem/525/A
# Rating : 1100

n=int(input())
s=input()
d,c=dict(),0
for i in range(0,2*n-2,2):
    if ord(s[i])-32 != ord(s[i+1]):
        d[s[i]]=d.get(s[i],0)+1
        if d.get(chr( ord(s[i+1]) + 32 ),0)!=0:
            d[chr(ord(s[i+1])+32)]-=1
        else:
            c+=1
print(c)

