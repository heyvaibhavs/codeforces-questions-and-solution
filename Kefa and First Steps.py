# Code by : Sam._.072

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    h=0
    c=1
    for i in range(1,n):
        if a[i-1]<=a[i]:
            c+=1
        else:
            if c>h:
                h=c
            c=1
    if c>h:
        h=c
    print(h)