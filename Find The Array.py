# problem name : Find The Array

for _ in range(int(input())):
    s=int(input())
    c,p=0,0
    while s>0:
        p+=2
        c+=1
        s-=p
    print(c)
