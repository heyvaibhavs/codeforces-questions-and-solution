for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if len(set(a))==1:
        print(0)
        continue
    f,h=101*[0],10000000000
    for i in range(1,max(a)+1):
        j=0
        while j<n:
            if a[j]!=i:
                break
            j+=1
        x,j=1,j+k
        # print("i= ",i,"j= ",j)
        while j<n:
            # print(a[j],end=" ")
            if a[j]!=i:
                x+=1
                j+=k
            else:
                j+=1
        if x<h:
            h=x
    print(h)




