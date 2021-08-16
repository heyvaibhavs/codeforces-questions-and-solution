for _ in range(int(input())):
    n,k=map(int,input().split())
    if (k%2==0 and n%2==0 and n>=k**2) or (k%2!=0 and n%2!=0 and n>=k**2):
        print("YES")
    else:
        print("NO")
