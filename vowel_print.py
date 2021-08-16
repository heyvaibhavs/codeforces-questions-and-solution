k=int(input())
if k<25:
    print(-1)
else:
    n,m=0,0
    for i in range(5,k):
        t=k/i
        if t>=5 and t-int(t)==0:
            n=int(t)
            m=i
            break
    if n==0 and m==0:
        print(-1)
    else:
        l=["aeiou","eioua","iouae","ouaei","uaeio"]
        l[0]+=(m-5)*"a"
        l[1]+=(m-5)*"e"
        l[2]+=(m-5)*"i"
        l[3]+=(m-5)*"o"
        l[4]+=(m-5)*"u"
        s1="aeiou"+(m-5)*"x"
        for i in range(n):
            if i<5:
                print(l[i],end="")
            else:
                print(s1,end="")



