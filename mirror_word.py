s=input()
s1=""
for i in s:
    if i=='A' or i=='H' or i=='I' or i=='M' or i=='O' or i=='T' or i=='U' or i=='V' or i=='W' or i=='X' or i=='Y':
        s1+=i
    else:
        print("NO")
        exit()
n=len(s1)
if n==0:
    print("NO")
    exit()
for i in range(n//2):
    if s1[i]!=s[n-1-i]:
        print("NO")
        exit()
print("YES")