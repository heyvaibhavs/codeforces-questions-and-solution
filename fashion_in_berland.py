n=int(input())
a=list(map(int,input().split()))
if n==1 and a[0]==1:
    print("YES")
elif a.count(1)==n-1 and n!=1: 
    print("YES")
else:
    print("NO")
