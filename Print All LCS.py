# Code by : Sam._.072

def LCS(i, j, s, t, l):
    if i == 0 or j == 0:
        return set([""])
    elif s[i-1] == t[j-1]:
        return set([Z + s[i-1] for Z in LCS(i-1, j-1, s, t, l)])
    else:
        R = set()
        if l[i][j-1] >= l[i-1][j]:
            R.update(LCS(i, j-1, s, t, l))
        if l[i-1][j] >= l[i][j-1]:
            R.update(LCS(i-1, j, s, t, l))
        return R


if __name__ == '__main__':
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    l = [[0 for i in range(m+1)]for j in range(n+1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif s[i - 1] == t[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])
    ans =LCS(n, m, s, t, l)
    ans = list(ans)
    print(ans)
