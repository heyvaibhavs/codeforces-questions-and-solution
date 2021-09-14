# problem name : Nuts
# problem link : https://codeforces.com/problemset/problem/402/A
# Rating : 1100

k,a,b,v=map(int, input().split())
c=b//(k-1)
b=b-c*(k-1)
if c*k*v>a:
    c=a//(k*v)
    if a%(k*v)!=0:
        c+=1
    print(c)
else:
    a=a- c*k*v
# print(a,c,b)
    if b>0:
        c+=1
        a-=(b+1)*v
    # print(a,c)
    if a>0:
        c+=a//v
    # print(a,c)
    if a%v!=0 and a>0:
        c+=1
    print(c)




