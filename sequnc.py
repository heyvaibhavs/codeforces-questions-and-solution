for _ in range(int(input())):
    n=int(input())
    s=input()
    s1=sorted(s)
    c=0
    for i in range(n):
        if s[i]!=s1[i]:
            c+=1
    print(c)


