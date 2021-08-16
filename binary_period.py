for _ in range(int(input())):
    s=input()
    # print(set(s),len(set(s)),len(s))
    if len(set(s))==1 or len(s)==2:
        print(s)
    else:
        s1=""
        for i in range(len(s)):
            s1+='10'
        print(s1)