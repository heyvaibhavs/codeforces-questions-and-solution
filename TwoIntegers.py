n=int(input())
a=list(map(int,input().split()))
h=max(a)
f=[]
for i in range(1,h+1):
    if h%i==0:
        f.append(i)
print(a-f)



