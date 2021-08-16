for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1:
        print(0)
        continue
    c,l=0,a[-1]
    for i in range(n-2,-1,-1):
        if a[i]>l:
            c+=1
        elif a[i]<l:
            l=a[i]
    print(c)

