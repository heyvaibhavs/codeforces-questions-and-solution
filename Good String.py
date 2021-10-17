# Code By : Sam._.072

n=int(input())
s=input()
i=1
ans=""
c=0
while i < n:
    if s[i]==s[i-1]:
        i+=1
        c+=1
    else:
        ans+=s[i-1]
        ans+=s[i]
        i+=2
if (n-c)%2!=0:
    c=c+1

if len(ans)==0:
    print(n)
elif len(ans)%2==0:
    print(c)
    print(ans)
else:
    print(c+1)
    print(ans[:-1])



