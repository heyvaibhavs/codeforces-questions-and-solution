# problem name : Luxurious Houses
# problem link : https://codeforces.com/problemset/problem/581/B
# Rating : 1100

n=int(input())
a=list(map(int, input().split()))
h=a[-1]
l=[h]
for i in range(n-2,-1,-1):
    if a[i]>=h:
        h=a[i]
        l.append(h)
h=l[-1]
for i in range(n-1):
    if a[i]<h:
        print(h-a[i]+1,end=" ")
    else:
        h1=h
        l.pop()
        h=l[-1]
        if h1==h:
            print(1,end=" ")
        else:
            print(0,end=" ")
print(0)

