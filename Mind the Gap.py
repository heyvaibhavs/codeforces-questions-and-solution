#problem name : Mind the Gap
#  problem link : https://codeforces.com/problemset/problem/967/A
# rating : 1100

n,s=map(int, input().split())
h=m=ph=pm=z=0
for i in range(n):
    ch,cm=map(int, input().split())
    if cm>=pm:
        c=cm-pm+(ch-ph)*60
    else:
        c=60-pm+cm+(ch-ph-1)*60
    if i==0 and c>=s+1:
        h,m=0,0
        z=-1
    if c>=2*s+2 and z==0:
        z=-1
        # print(c)
        if pm+s+1>=60:
            h,m=ph+(pm+s+1)//60,(pm+s+1)%60
        else:
            h,m=ph,pm+s+1
    ph,pm=ch,cm
if z==-1:
    print(h,m)
else:
    if (pm+s+1)>=60:
        print(ph+(pm+s+1)//60,(pm+s+1)%60)
    else:
        print(ph,pm+s+1)




