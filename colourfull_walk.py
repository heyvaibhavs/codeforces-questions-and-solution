n=int(input())
a=list(map(int,input().split()))
h=0
for i in range(n):
    c=0
    for j in range(i+1,n):
        if a[i]!=a[j] and j-i>c:
            c=j-i 
    if c>h:
        h=c
print(h)