for _ in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    c0=a[-1]*a[-2]*a[-3]*a[-4]*a[-5]
    c1=a[0]*a[-1]*a[-2]*a[-3]*a[-4]
    c2=a[0]*a[1]*a[-1]*a[-2]*a[-3]
    c3=a[0]*a[1]*a[2]*a[-1]*a[-2]
    c4=a[0]*a[1]*a[2]*a[3]*a[-1]
    c5=a[0]*a[1]*a[2]*a[3]*a[4]
    # print(c0,c1,c2,c3,c4,c5)
    print(max(c0, c1,c2,c3,c4,c5))

        
