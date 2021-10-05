# problem name : Challenging Cliffs
# problem link : https://codeforces.com/problemset/problem/1537/C
# Rating : 1200

for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    x,y=-1,-1
    for i in range(n-1):
        if a[i]==a[i+1]:
            x=i
            y=i+1
            break
    if n==2:
        print(*a,end=" ")
    elif x==-1 and y==-1:
        x=a[1]-a[0]
        y=0
        for i in range(1,n-1):
            if a[i+1]-a[i]<x:
                x=a[i+1]-a[i]
                y=i
        print(a[y+1],end=" ")
        for i in range(n):
            if i!=y and i!=y+1:
                print(a[i],end=" ")
        print(a[y],end=" ")

    elif n==4:
        if x==2:
            print(a[2],a[0],a[1],a[3],end=" ")
        elif x==1:
            print(a[1],a[3],a[0],a[2],end=" ")
        else:
            print(a[0],a[2],a[3],a[1],end=" ")
    else:
        print(a[x],end=" ")
        for i in range(n):
            if i!=x and i!=y:
                print(a[i],end=" ")
        print(a[y],end=" ")
    print()
