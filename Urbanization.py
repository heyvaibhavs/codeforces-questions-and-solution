# problem name : Urbanization
# problem link : https://codeforces.com/problemset/problem/735/B
# Rating : 1100

n,n1,n2=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
if n1<=n2:
    x=y=k=0
    for i in range(n-n1-n2,n):
        if k<n2:
            x+=a[i]
        else:
            y+=a[i]
        k+=1
    print(x/n2+y/n1)
else:
    x=y=k=0
    for i in range(n-n1-n2,n):
        if k<n1:
            x+=a[i]
        else:
            y+=a[i]
        k+=1
    print(x/n1+y/n2)
