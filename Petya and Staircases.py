# problem name : Petya and Staircases
# problem link : https://codeforces.com/problemset/problem/362/B
# Rating : 1100

n,m=map(int, input().split())
if m!=0:
    a=list(map(int, input().split()))
    a.sort()
if m==0:
    print("YES")
elif a[0]==1 or a[-1]==n:
    print("NO")
else:   
    c=0
    # print(a)
    for i in range(m-1):
        if a[i+1]-a[i]==1:
            c+=1
        else:
            c=0
        if c>=2:
            break
        # print(c,i)
    if c>=2:
        print("NO")
    else:
        print("YES")




