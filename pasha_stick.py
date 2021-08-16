n=int(input())
if n<=5:
    print(0)
elif n%2==0 and (n//2)%2==0:
    print(n//4-1)
elif n%2==0 and (n//2)%2!=0:
    print(n//4)
else:
    print(0)



