# problem name : Akku and Binary Numbers
# problem link : https://practice.geeksforgeeks.org/problems/akku-and-binary-numbers0902/0/
# level : easy

l,r=map(int,input().split())
ans=[]
for i in range(63):
    x=1<<i
    for j in range(i+1,63):
        y=1<<j
        for k in range(j+1,63):
            v=(1<<k)|x|y
            ans.append(v)
ans.sort()
print(br(ans,r)-bl(ans,l))