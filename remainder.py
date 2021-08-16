n,x,y=map(int,input().split())
s=input()
s1=s[n-x:]
s2=(x-y-1)*"0"+"1"+y*"0"
c=0
for i in range(x):
    if s1[i]!=s2[i]:
        c+=1
print(c)


