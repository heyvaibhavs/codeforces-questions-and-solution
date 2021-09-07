# problem name : Lucky numbers
# problem lnik : https://codeforces.com/problemset/problem/630/C
# Rating : 1100

n=int(input())
c=0
for i in range(1,n+1):
    c+=2**i
print(c) 