a,b=map(int,input().split())
c=0
l=[6,2,5,5,4,5,6,3,7,6]
while a<=b:
    t=a
    while t>0:
        c+=l[t%10]
        t=t//10
    a+=1
print(c)

