for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x,i=1,0
    if a[0]==1:
        while i<n:
            if i%2==0 and a[i]==1:
                x=1
            elif i%2!=0 and a[i]==1:
                x=-1
            else:
                if x==1:
                    x=-1
                else:
                    x=1
                break
            i+=1
    if (i==n and n%2==0) or (i==n-1 and x==-1):
        print("Second")
    elif (i==n and n%2!=0) or (i==n-1 and x==1):
        print("First")
    else:
        if x==1:
            print("First")
        else:
            print("Second")
        


