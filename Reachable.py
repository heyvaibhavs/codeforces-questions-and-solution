n=int(input())
c=0
if n%10==0:
    n+=1
    c=1
while n>10:
    t=n%10
    n=n//10
    if t>0:
        c+=10-t
        n+=1
    # print(n,t,c)
print(c+9)
