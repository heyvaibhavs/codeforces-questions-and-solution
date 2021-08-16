n=int(input())
x=int(input())
if x==0:
    if n%6==3 or n%6==4:
        print(2)
    elif n%6==1 or n%6==2:
        print(1)
    elif n%6==5 or n%6==0:
        print(0)
elif x==1:
    if n%3==0:
        print(1)
    elif n%3==1:
        print(0)
    elif n%3==2:
        print(2)
else:
    if n%6==0 or n%6==1:
        print(2)
    elif n%6==4 or n%6==5:
        print(1)
    elif n%6==2 or n%6==3:
        print(0)
