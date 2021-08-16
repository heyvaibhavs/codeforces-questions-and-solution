def hash(s):
    p=31
    mod=1e9+7
    ans=0
    for i in s:
        ans+=((ord(i)-ord("a")+1)*(p%mod))%mod
        ans%=mod
        p*=31
        p%=mod
    return int(ans%mod)

s=input()
n=len(s)
f=26*[0]
for i in s:
    f[ord(i)-97]+=1
s1=""
j,n=0,len(s)
for i in range(n):
    if f[ord(s[i])-97]==1:
        while j<i:
            if s[j]>s[i] and f[ord(s[j])-97]>0:
                s1+=s[j]
                f[ord(s[j])-97]=0
            j+=1
        s1+=s[i]
        f[ord(s[i])-97]=0
        j=i
    else:
        f[ord(s[i])-97]-=1
print(s1) 
print(hash(s1))

