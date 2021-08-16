def lucky_no(i,p):
    if p%i==0:
        return 0
    elif p<i:
        return 1
    else:
        p=p-p//i
        i+=1
        return lucky_no(i,p)
t=int(input())
while t>0:
    n=int(input())
    print(lucky_no(2,n))
    t-=1