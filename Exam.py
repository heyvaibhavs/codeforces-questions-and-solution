# problem name : Exam
# problem link : https://codeforces.com/problemset/problem/534/A
# Rating : 1100

n=int(input())
if n==1 or n==2:
    print(1)
    print(1)
elif n==3:
    print(2)
    print(1,3)
elif n==4:
    print(4)
    print(3,1,4,2)
else:
    print(n)
    for i in range(1,n+1,2):
        print(i,end=" ")
    for i in range(2,n+1,2):
        print(i,end=" ")



