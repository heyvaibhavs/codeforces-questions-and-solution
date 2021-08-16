n=int(input())
s=input()
a=list(map(int,input().split()))
f=n*[False]
i,j=0,0
while True:
    # print(i,f[i])
    if i<0 or i>=n or n==1:
        print("FINITE")
        break
    elif  f[i]==True:
        print("INFINITE")
        break
    else:  
        f[i]=True
        if s[i]=='>':
            i+=a[i]
        else:
            i-=a[i]


