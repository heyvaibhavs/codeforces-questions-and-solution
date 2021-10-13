import sys
for _ in range(int(input())):
    n=input()
    a=list(n)
    a.reverse()
    c1,c2,c3,c4=20,20,20,20
    if '5' in a and '0' in a:
        x=0
        y=-1
        for i in range(len(a)):
            if x==0 and a[i]=='0':
                x=-1
                y=i
            elif x==-1 and a[i]=='5':
                c1=y+i-y-1
                break
    if '2' in a and '5' in a:
        x=0
        y=-1
        for i in range(len(a)):
            if x==0 and a[i]=='5':
                x=-1
                y=i
            elif x==-1 and a[i]=='2':
                c2=y+i-y-1
                break
    if '7' in a and '5' in a:
        x=0
        y=-1
        for i in range(len(a)):
            if x==0 and a[i]=='5':
                x=-1
                y=i
            elif x==-1 and a[i]=='7':
                c3=y+i-y-1
                break
    if '0' in a:
        x=0
        y=-1
        for i in range(len(a)):
            if x==0 and a[i]=='0':
                x=-1
                y=i
            elif x==-1 and a[i]=='0':
                c4=y+i-y-1
                break

    print(min(c1,c2,c3,c4))
    

