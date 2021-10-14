# Code by : Sam._.072

for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        l.append(list(map(int,input().split())))
    f=[]
    for i in range(5):
        c=[]
        for j in range(n):
            if l[j][i]==1:
                c.append(j+1)
        f.append(c)
    del l,c
    z=0
    for i in range(5):
        for j in range(i+1,5):
            if len(f[i])>=n//2 and len(f[j])>=n//2:
                s=(set(f[i])|(set(f[j])))
                if len(s)==n:
                    z=-1
                    break
        if z==-1:
            break
    if z==-1:
        print("YES")
    else:
        print("NO")



    
