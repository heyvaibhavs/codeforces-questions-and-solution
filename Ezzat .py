for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    h=max(a)
    print(h+(sum(a)-h)/(n-1))
