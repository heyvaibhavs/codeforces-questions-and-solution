# problem name : Min Mex cut
# problem link : https://codeforces.com/contest/1566/problem/B

for i in range(int(input())):
    s=input()
    n=len(s)
    c=s.count('0')
    s1=c*'0'
    # print(s1)
    if s1 in s and c>0:
        print(1)
    elif c>1:
        print(2)
    else:
        print(c)