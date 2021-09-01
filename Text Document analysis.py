# problem name : Text Document analysis
# problem link : https://codeforces.com/problemset/problem/723/B
# Rating : 1100

n=int(input())
s=input()
x=0
if s[0]=='(':
    x=-1
h1,h2,i,c=0,0,0,0
while i <n:
    if s[i]=='(':
        x=-1
        i+=1
        if c>h1:
            h1=c
        c=0
    elif s[i]==')':
        x=0
        i+=1
    else:
        if x==0 and i<n :
            if s[i]=='_':
                if c>h1:
                    h1=c
                c=0
            else:
                c+=1
            i+=1
        elif x==-1 and i<n:
            if s[i]=='_' and i-1>=0 and ( (ord(s[i-1])>=65 and ord(s[i-1])<=90) or (ord(s[i-1])>=97 and ord(s[i])<=122) ):
                h2+=1
                # print(h2,i,"f")
            i+=1
            if i<n and s[i]==')' and i-1>=0 and ( (ord(s[i-1])>=65 and ord(s[i-1])<=90) or (ord(s[i-1])>=97 and ord(s[i])<=122) ):
                h2+=1
                # print(h2,i,"s")
                x=0
                i+=1
    # print(i,x)
            
if c>h1:
    h1=c
print(h1,h2)
