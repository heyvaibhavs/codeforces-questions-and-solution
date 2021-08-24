# problem name : Nearest Minimums
# problem link : https://codeforces.com/problemset/problem/911/A
# problem rating : 1100

n=int(input())
a=list(map(int, input().split()))
x=min(a)
h=n+1
p=a.index(x)
# print(p)
for i in range(p+1,n):
    if a[i]==x:
        # print(i,i-p)
        if i-p<h:
            h=i-p
        p=i
print(h)


