# Code by : Sam._.072

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    ans = [a]
    k, t = n, n//2
    while t > 1:
        if k == b or k == a:
            k -= 1
        else:
            ans.append(k)
            k -= 1
            t -= 1
    t = n//2
    ans.append(b)
    while t > 1:
        if k == a or k == b:
            k -= 1
        else:
            ans.append(k)
            k -= 1
            t -= 1
    if len(ans)==n and min(ans[:n//2])==a and max(ans[n//2:])==b:
        print(*ans)
    else:
        print(-1)

