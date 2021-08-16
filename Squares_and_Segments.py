n=int(input())
if n==1:
    print(2)
elif n==2:
    print(3)
elif n==3 or n==4:
    print(4)
elif n==5 or n==6:
    print(5)
else:
    t=n**0.5
    if t-int(t)==0:
        print(2*int(t))
    else:
        t=int(t)
        if n<=t*t+t:
            print(2*t+1)
        else:
            print(2*t+2)