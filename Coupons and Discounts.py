# problem name : Coupons and Discounts
# problem link : https://codeforces.com/problemset/problem/731/B
# Rating : 1100

n=int(input())
a=list(map(int, input().split()))
x=i=0
while i < n:
    if i+1<n and a[i]%2!=0 and a[i+1]%2!=0 and a[i+1]!=0:
        a[i+1]=0
        i+=2
    elif i+1<n and a[i]%2!=0 and a[i+1]%2==0 and a[i+1]!=0:
        a[i+1]-=1
        i+=1
    elif a[i]%2==0:
        a[i]=0
        i+=1
    else:
        x=-1
        break
    # print(a)
if x==0:
    print("YES")
else:
    print("NO")




