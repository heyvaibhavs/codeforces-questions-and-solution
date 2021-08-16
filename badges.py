b=int(input())
g=int(input())
n=int(input())
c=0
if n%2==0:
    n1=n//2
    if n1<=b and n1<=g:
        c+=1
else:
    n1=n//2+1
for i in range(n1):
    if i<=b and n-i<=g and i<=g and n-i<=b:
        c+=2
    elif(i<=b and n-i<=g) or (i<=g and n-i<=b):
        c+=1
    # print(c)
print(c)
