n=int(input())
a=list(map(int,input().split()))
a.sort()
l=[]
for i in range(n//2):
    if a[i]<=a[n-1-i]:
        l.append(a[i])
        l.append(a[n-1-i])
    else:
        print("impossible")
        exit()
# print(n)
if n%2!=0:
    l.append(a[n//2])
print(*l)