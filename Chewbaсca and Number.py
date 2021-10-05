s=input()
n=len(s)
x=''
for i in range(n):
    if (i==0 and s[i]=='9') or (ord(s[i])>=48 and ord(s[i])<=52):
        x += s[i]
    else:
        x += str(57-ord(s[i]))
print(x)