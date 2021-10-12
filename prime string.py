s=input()
n=len(s)
c1,c2=0,0
for i in range(n):
    if i%2==0:
        c1+=ord(s[i])
    else:
        c2+=ord(s[i])
# print(c1,c2)
d=abs(c1-c2)
if d%3==0 or d%5==0 or d%7==0:
    print("PRIME STRING")
else:
    print("CASUAL STRING")