n,t=map(int,input().split())
if n==1 and t==10:
    print(-1)
elif t==10:
    s='1'+(n-1)*'0'
    print(s)
else:
    print(n*str(t))