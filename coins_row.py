for _ in range(int(input())):
    m=int(input())
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
    s=sum(a1)
    h,x=[],0
    for i in range(m):
        s-=a1[i]
        # print(s,x)
        h.append(max(s,x))
        x+=a2[i]
    # print(h)        
    if len(h)==0:
        print(0)
    else:
        print(min(h))        
