# problem name : Intresting Drink
# problem link : https://codeforces.com/problemset/problem/706/B
# Rating : 1100

def freq(a,n):
    f=(a[-1]+1)*[0]
    f[a[0]]=1
    p=a[0]+1
    for i in range(1,n):
        f[a[i]]=i+1
        for j in range(p,a[i]):
            f[j]=i
        p=a[i]+1
    return f

n=int(input())
a=list(map(int,input().split()))
a.sort()
f=freq(a, n)
q=int(input())
for i in range(q):
    x=int(input())
    if x >a[-1]:
        print(n)
    else:
        print(f[x])



