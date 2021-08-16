import math
n,x=map(int,input().split())
c,i=0,1
while i <=math.sqrt(x):
    if x%i==0 and i<=n and x/i<=n:
        if i !=x//i:
            c+=2
        else:
            c+=1
    i+=1
print(c)
