# Code By : Sam._.072

for _ in range(int(input())):
    n=int(input())
    s1=input()
    s2=input()
    z=0
    for i in range(n-1):
        if s1[i]=='1' and s2[i]=='1':
            z=-1
            break
    if z==0:
        print("YES")
    else:
        print("NO")
