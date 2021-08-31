# problem name : metting of old Friends
# problem link : https://codeforces.com/problemset/problem/714/A
# Rating : 1100

l1,r1,l2,r2,k=map(int,input().split())
if l2 >r1 or r2<l1:
    print(0)
elif l2 >= l1 and l2<=r1 and r2>=r1:
    if k>=l2 and k<=r1:
        print(r1-l2)
    else:
        print(r1-l2+1)
elif l2>=l1 and r2<=r1:
    if k>=l2 and k<=r2:
        print(r2-l2)
    else:
        print(r2-l2+1)
elif l2<=l1 and r2>=l1 and r2<=r1:
    if k>=l1 and k<=r2:
        print(r2-l1)
    else:
        print(r2-l1+1)
elif l2<=l1 and r2>=r1:
    if k>=l1 and k<=r1:
        print(r1-l1)
    else:
        print(r1-l1+1)
