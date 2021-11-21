# Code by : Sam._.072

for _ in range(int(input())):
    a, b =map(int, input().split())
    s = input()
    for i in s:
        if i=='0':
            a -= 1
        elif i =='1':
            b -= 1
    s = list(s)
    i, j = 0, len(s)-1
    while i < j:
        if s[i]=='0' and s[j]=='?':
            s[j] = '0'
            a -= 1
        elif s[i]=='?' and s[j]=='0':
            s[i] = '0'
            a -= 1
        elif s[i] == '1' and s[j] == '?':
            s[j] = '1'
            b -= 1
        elif s[i] == '?' and s[j] == '1':
            s[i] = '1'
            b -= 1
        i += 1
        j -= 1
    i, j = 0, len(s)-1
    z = 0
    while i<j:
        if s[i]==s[j] and s[i]!='?':
            i += 1
            j -= 1
            continue
        elif s[i] == s[j] and s[i]=='?':
            if a>=2:
                s[i] = '0'
                s[j] = '0'
                a -= 2
            elif b >= 2:
                s[i] = '1'
                s[j] = '1'
                b -= 2
            else:
                z = -1
                break
        elif s[i] != s[j]:
            if (s[i]=='0' and s[j]=='1') or (s[i]=='1' and s[j]=='0'):
                z = -1
                break
            elif s[i]=='0' and s[j]=='?' and a>0:
                s[j] = '0'
                a -= 1
            elif s[i]=='?' and s[j]=='0' and a>0:
                s[i] = '0'
                a -= 1
            elif s[i]=='1' and s[j]=='?' and b>0:
                s[j] = '1'
                b -= 1
            elif s[i]=='?' and s[j]=='1' and b>0:
                s[i]='1'
                b -= 1
            else:
                z = -1
                break
        i += 1
        j -= 1
    if len(s)%2!=0:
        n = len(s)//2
        if s[n] =='?':
            if a>0:
                s[n]='0'
                a -= 1
            elif b>0:
                s[n]='1'
                b -= 1
            else:
                z = -1   
    if z == 0 and a ==0 and b ==0 and s==s[::-1]:
        print(''.join(s))
    else:
        print(-1)

            
    