n=int(input())
a=list(map(int,input().split()))
c1,c2,c3,c4=0,0,0,0
for i in range(n):
    if a[i]==4:
        c4+=1
    elif a[i]==3:
        c3+=1
    elif a[i]==2:
        c2+=1
    else:
        c1+=1
if c2%2==0 and c2!=0:
    c2=c2//2
elif c2!=0 and c2%2!=0:
    c2=c2//2+1
    c1-=2
# print(c1,c2,c3,c4)
if c1<=c3:
    print(c4+c3+c2)
else:
    if (c1-c3)%4==0:
        c1=(c1-c3)//4
    else:
        c1=(c1-c3)//4+1
    print(c4+c2+c3+c1)


