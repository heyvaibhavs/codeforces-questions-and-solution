for _ in range(int(input())):
    s=input()
    d,p,x=0,0,-1
    for i in range(len(s)):
        if s[i]=='R':
            if i-x>d:
                d=i-x
            x=i
    if len(s)-x>d:
        d=len(s)-x
    print(d)
