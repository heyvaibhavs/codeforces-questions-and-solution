# problem name : Alyona and Numbers
# problem link : https://codeforces.com/problemset/problem/682/A
# Rating : 1100

n,m=map(int, input().split())
f1=[n//5 for i in range(5)]
f2=[m//5 for i in range(5)]
for i in range(n%5):
    f1[i]+=1
for i in range(m%5):
    f2[i]+=1
print(f1[0]*f2[3] + f1[1]*f2[2] + f1[2]*f2[1] + f1[3]*f2[0] + f1[4]*f2[4])



