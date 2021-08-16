n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(input())
x,y=[],[]
p=""
for i in range(n):
    if l[i]!='1':
        t1=l[i]
        z=0
        for j in range(i+1,n):
            t=l[j]
            z2=0
            if t!='1':
                for k in range(m):
                    # print(t1,t)
                    if t1[k]!=t[m-1-k]:
                        z2=-1
                        break
                if z==0 and z2==0:
                    x.append(t1)
                    y.append(t)
                    l[j]='1'
                    break
        if len(p)==0:
            z1=0
            for j in range(m//2):   
                if t1[j]!=t1[m-1-j]:
                    z1=-1
                    break
            if z1==0:
                p=t1
print((len(x)+len(y))*m+len(p))
for i in x:
    print(i,end="")
if len(p)!=0:
    print(p,end="")
for i in range(len(y)-1,-1,-1):
    print(y[i],end="")




