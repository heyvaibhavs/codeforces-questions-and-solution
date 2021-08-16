s=input()
h,p=-1,-1
for i in range(len(s)):
    if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U' or s[i]=='Y':
        if i-p>h:
            h=i-p
        p=i
if len(s)-p>h:
    h=len(s)-p
print(h)