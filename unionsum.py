def subsum(n,a):
    j,c,p=0,0,1
    while n>0:
        last_bit=n&1
        if last_bit==1:
            p=p*a[j]
        j+=1
        n=n>>1
    return p
a=[2,3,5]
ans =0
for i in range(1,8):
    p=subsum(i,a)
    if (bin(i).count('1'))%2==0:
        ans-=999//p
    else:
        ans+=999//p
print(ans)