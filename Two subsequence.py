for _ in range(int(input())):
    s=input()
    f=26*[0]
    x,y='',''
    for i in s:
        f[ord(i)-97]+=1
    for i in range(26):
        if f[i]>0:
            x=chr(i+97)
            f[i]-=1
            break
    for i in s:
        if f[ord(i)-97]>0:
            f[ord(i)-97]-=1
            y+=i
    print(x,y)
    