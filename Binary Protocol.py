# problem name : Binary Protocol
# problem link : https://codeforces.com/problemset/problem/825/A
# rating : 1100

n=int(input())
s=input()
c=i=0
while i<n:
    if s[i]=='1':
        c+=1
    else:
        print(c,end="")
        if i+1<n and s[i+1]=='0':
            i+=1
            print(0,end="")
        c=0
    i+=1
print(c)


