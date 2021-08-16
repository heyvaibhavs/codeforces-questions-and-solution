a=int(input())
b=int(input())
n=a+b+1
if a==0 and b>0:
    while n>0:
        print(n,end=" ")
        n-=1
elif a>0 and b==0:
    i=1
    while i<=n:
        print(i,end=" ")
        i+=1
else:
    i=b+2
    print(1,end=" ")
    while a>0:
        print(i,end=" ")
        i+=1
        a-=1
    i=b+1
    while b>0:
        print(i,end=" ")
        i-=1
        b-=1
        

