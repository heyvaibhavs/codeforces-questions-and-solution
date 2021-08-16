for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    y=0
    for i in range(n):
       y+=a[i]
       if y/(i+1)<x:
           y=-1
           print(i)
           break
    if y!=-1:
        print(n)