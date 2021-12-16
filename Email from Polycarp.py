# problem name : Email from Polycarp
# problem link : https://codeforces.com/contest/1185/problem/B
# Rating : 1200

def Check(s, t):
    i, n = 0, len(s)
    j, m = 0, len(t)
    while i < n or j < m:
        c1, c2 = 0, 0
        k = s[i]
        while i < n:
            if s[i] == k:
                c1 += 1
            else: break
            i += 1
        while j < m:
            if t[j] == k:
                c2 += 1
            else: break
            j += 1
        if c1 > c2 or (i == n and j < m):
            return False 
    return True


for _ in range(int(input())):
    s=input()
    t=input()
    if s == t or Check(s, t):
        print("YES")
    else:
        print("NO")

