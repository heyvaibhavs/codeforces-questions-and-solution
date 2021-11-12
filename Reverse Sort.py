# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    s = input()
    a = ''.join(sorted(s))
    if s==a:
        print(0)
    else:
        print(1)
        c,ans=0,[]
        for i in range(n):
            if s[i]!=a[i]:
                c+=1
                ans.append(i+1)
        print(c,*ans)