for i  in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x,y,z=0,0,0
    for i in range(2*n):
        if a[i]==0:
            z+=1
        elif a[i]%2==0 :
            x+=1
        else:
            y+=1
    # print(z,x,y)
    if  z+x==y:
        print("YES")
    else:
        print("NO") 