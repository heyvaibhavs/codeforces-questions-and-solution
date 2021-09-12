# problem name : A and B and Compilation Errors
# problem link : https://codeforces.com/problemset/problem/519/B
# Rating : 1100

n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))
print(sum(a)-sum(b))
print(sum(b)-sum(c))


