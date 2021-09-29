# problem name : Permutation Minimization by Deque
# problem link : https://codeforces.com/contest/1579/problem/E1

from collections import deque
for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    l=deque()
    l.append(a[0])
    for i in range(1,n):
        if a[i]<l[0]:
            l.appendleft(a[i])
        else:
            l.append(a[i])
    print(*l)


