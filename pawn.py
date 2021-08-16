for _ in range(int(input())):
    n=int(input())
    x=input()
    y=input()
    s=list(x)
    s1=list(y)
    c=0
    if s1[0]=='1':
        if s[0]=='0':
            c+=1
        elif s[1]=='1':
            c+=1
            s[1]='x'
    if s1[-1]=='1':
        if s[-1]=='0':
            c+=1
        elif s[-2]=='1':
            c+=1
            s[-2]='x'
    c1,c2=0,0
    for i in range(1,n-1):
        if s1[i]=='1':
            if s[i]=='0':
                c1+=1
            elif s[i-1]=='1':
                s[i-1]='x'
                c1+=1
            elif s[i+1]=='1':
                s[i+1]='x'
                c1+=1
    # for i in range(1,n-1):
    #     if s1[i]=='1':
    #         if s[i]=='0':
    #             c2+=1
    #         elif s[i+1]=='1':
    #             s[i+1]='x'
    #             c2+=1
    #         elif s[i-1]=='1':
    #             s[i-1]='x'
    #             c2+=1
    print(c+c1)
