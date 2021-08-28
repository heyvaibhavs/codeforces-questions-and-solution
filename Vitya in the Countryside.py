# problem name : Vitya in the Countryside
# problem link : https://codeforces.com/problemset/problem/719/A
# Rating : 1100

n=int(input())
a=list(map(int, input().split()))

if a[-1]==0 or (n>1 and a[-1]>a[-2]):
    print("UP")
elif a[-1]==15 or ( n>1 and a[-1]<a[-2]):
    print("DOWN")
else:
    print(-1)