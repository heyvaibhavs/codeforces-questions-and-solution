for _ in range(int(input())):
    n,m=map(int,input().split())
    f=26*[0]
    l=[]
    for i in range(n):
        s=input()
        l.append(s)
        for j in range(m):
            f[ord(s[j])-97]+=1
    for i in range(n-1):
        s=input()
        for j in range(m):
            f[ord(s[j])-97]-=1
    for i in range(n):
        s=l[i]
        f1=26*[0]
        for j in range(m):
            f1[ord(s[j])-97]+=1
        if f1==f:
            print(s)
            break