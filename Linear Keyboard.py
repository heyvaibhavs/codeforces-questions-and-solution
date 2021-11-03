# Code by : Sam._.072

for _ in range(int(input())):
    k = input()
    s = input()
    f = 26*[0]
    for i in range(26):
        f[ord(k[i])-97] = i
    c=0
    p=f[ord(s[0])-97]
    for i in range(1,len(s)):
        c +=abs(p-f[ord(s[i])-97])
        p=f[ord(s[i])-97]
    print(c) 

    