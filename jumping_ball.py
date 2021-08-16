n=int(input())
s=input()
x,y=0,0
for i in range(n):
    if s[i]=='<':
        x+=1
    else:
        break
for i in range(n-1,-1,-1):
    if s[i]=='>':
        y+=1
    else:
        break
print(x+y)