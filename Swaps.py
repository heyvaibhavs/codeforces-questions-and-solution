for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    if a[0]<b[0]:
        print(0)
        continue
    # elif a[1] < b[0] or a[0] < b[1]:
    #     print(1)
    #     continue
    f=(2*n)*[-1]
    for i in range(n):
        if a[i]==1:
            f[a[i]]=i
        elif f[a[i]-2]==-1:
            f[a[i]]=i
        else:
            f[a[i]]=f[a[i]-2]
    c1=2*n
    # print(f)
    for i in range(n):
        c=f[b[i]-1]
        if c + i < c1:
            c1=c+i
            # print(c1)
    print(c1)


