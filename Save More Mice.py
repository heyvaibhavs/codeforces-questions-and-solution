# Code by : Sam._.072

for _ in range(int(input())):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    a.sort()
    axix = [0 for i in range(n)]
    x=0
    c=0
    while x<n:
        a[-1]+=1
        if a[-1]==n and a[-1]!=0:
            c+=1
            a.pop()
        x+=1
        if a[0]==x:
            for i in range(len(a)):
                if a[i]==x:
                    a[i]=0
                else:
                    break

    print(c)
    