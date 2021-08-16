s=input()
c,i,j=0,0,len(s)-1
while i <j:
    if s[i]!=s[j]:
        c+=1
    if c>2:
        break
    i+=1
    j-=1
if (c<=1 and len(s)%2!=0) or (len(s)%2==0 and c==1):
    print("YES")
else:
    print("NO")
