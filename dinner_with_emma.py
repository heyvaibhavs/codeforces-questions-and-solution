n,m=map(int,input().split())
l,x=[],[]
for i in range(n):
    l.append(list(map(int,input().split())))
    x.extend(l[i])
if n==1:
    print(min(l[0]))
elif m==1:
    print(*max(l))
else:
    x=list(set(x))
    x.sort()
    # print(x)
    c=0
    for i in range(len(x)):
        for j in range(n):
            if l[j]!=-1 and x[i] in l[j]:
                l[j]=-1
                c+=1

        if c==n:
            print(x[i])
            break
        elif c==n-1:
            for i in range(n):
                if l[i]!=-1:
                    print(min(l[i]))
            break
        

