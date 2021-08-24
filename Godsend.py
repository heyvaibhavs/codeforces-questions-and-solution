# problem name : Godsend
# problem link : https://codeforces.com/problemset/problem/841/B
# rating : 1100

n=int(input())
a=list(map(int, input().split()))
c=0
for i in a:
    if i%2!=0:
        c+=1
if c==0:
    print("Second")
else:
    print("First")