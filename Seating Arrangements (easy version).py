# problem name : Seating Arrangements (easy version)
# problem link : https://codeforces.com/contest/1566/problem/D1

def inconv(f,n):
    c=0
    for i in f:
        if i <n:
            c+=f[i]
    # print(c)
    return c

for  i in  range(int(input())):
    n,m=map(int, input().split())
    a=list(map(int, input().split()))
    f=dict()
    c=0
    for i in a:
        c+=inconv(f, i)
        f[i]=f.get(i,0)+1
    print(c)



