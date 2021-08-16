for _ in range(int(input())):
    s=input()
    if len(set(s))!=len(s):
        print("NO")
    else:
        n=len(s)
        a=26*[-1]
        for i in range(n):
            a[ord(s[i])-97]=i
        z=0
        for i in range(26):
            if a[i]>=0:
                z+=1
            else:
                break
        if z!=n:
            print("NO")
        # elif z==1 and a[0]==0:
            # print("YES")
        else:
            z=0
            for i in range(a[0]-1,0,-1):
                if s[i-1]<s[i]:
                    z=-1
                    break
            for i in range(a[0],n-1):
                if s[i+1]<s[i]:
                    z=-1
                    break
            if z==0:
                print("YES")
            else:
                print("NO")