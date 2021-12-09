# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = 'a'*50
    print(s)
    s = list(s)
    for i in range(n):
        if s[a[i]]=='a':
            s[a[i]]='b'
        else:
            s[a[i]]='a'
        print(''.join(s))
        