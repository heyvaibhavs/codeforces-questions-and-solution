for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n==2:
        if a[1]-a[0]==1 or (a[0]%2==0 and a[1]%2==0):
            print("YES")
        else:
            print("NO")
        continue
    x=0

    for i in range(n):
        if a[i]%2!=0:
            x+=1
    if x%2==0:
        print("YES")
    else:
        a.sort()
        x=0
        for i in range(n-1):
            if a[i+1]-a[i]==1:
                x=-1
                break
        if x==-1:
            print("YES")
        else:
            print("NO")     