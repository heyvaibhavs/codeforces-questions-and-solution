# problem name : Restrictive Candy Crush 
# problem link : https://practice.geeksforgeeks.org/problems/8c8f95810b05b4cab665f2997d36991bd58308a2/1/?track=md-stack&batchId=144

k=int(input())
s=input()
s1=[]
for i in s:
    if len(s1)==0:
        s1.append(i)
    elif s1[-1]!=i:
        s1.append(i)
    else:
        c=1
        for j in range(len(s1)-1,-1,-1):
            if s1[j]==i:
                c+=1
        if c==k:
            for j in range(k-1):
                s1.pop()
        else:
            s1.append(i)


print("".join(s1))
    
