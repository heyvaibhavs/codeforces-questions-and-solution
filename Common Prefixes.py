# Code by : Sam._.072

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = ['' for i in range(n+1)]
    x = 0
    for i in range(n):
        if i == 0:
            if a[i]==0:
                ans[0]='a'
                ans[1]='b'
            else:
                ans[0] = a[i]*'a'
                ans[1] = a[i]*'a'
        elif a[i]==0:
            if ans[i][0]=='a':
                ans[i+1]='b'
            else:
                ans[i+1]='a'
        elif a[i]>a[i-1]:
            if i>=1:
                if i-2>0 and a[i-2]>a[i] and ans[i-1][a[i]-1]=='x':
                    ans[i+1] = ans[i] + 'y'*(a[i]-len(ans[i]))
                    ans[i] = ans[i+1]
                else:
                    ans[i+1] = ans[i] + 'x'*(a[i]-len(ans[i]))
                    ans[i] = ans[i+1]
            else:
                ans[i+1] = ans[i] + 'z'*(a[i]-len(ans[i]))
                ans[i] = ans[i+1]
                x = 0


        else:
            ans[i+1] = ans[i][:a[i]]
    for i in ans:
        print(i)
