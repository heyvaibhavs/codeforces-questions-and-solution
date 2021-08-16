s=input()
if len(set(s))==1 and s[0]=='a':
    print(s)
elif not('a' in s) and len(s)%2==0:
    if s[:len(s)//2]==s[len(s)//2:]:
        print(s[:len(s)//2])
    else:
        print(":(")
elif s[-1]=='a':
    print(":(")
else:
    s1=s2=""
    x=-1
    for i in range(len(s)-1,-1,-1):
        if s[i]=='a':
            x=i
            break
        else:
            s2+=s[i]
    # print("x=",x)
    for i in range(x+1):
        if s[i]!='a':
            s1+=s[i]
    n=len(s1)+len(s2)
    # print(s1,s2,n)
    if n%2==0 and n>0:
        if len(s1)<=len(s2):
            for i in range(len(s2)-1,n//2-1,-1):
                s1+=s2[i]
            s2=s2[:n//2]
            z=0
            # print(s1,s2)
            for i in range(n//2):
                if s1[i]!=s2[n//2-1-i]:
                    z=-1
                    break
            if z==0:
                print(s[:len(s)-n//2])
            else:
                print(":(")
        else:
            print(":(")

    else:
        print(":(")


