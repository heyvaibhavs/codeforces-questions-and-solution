n,m=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
for i in range(n):
    if s[i] in t:
        print(s[i],end=" ")

