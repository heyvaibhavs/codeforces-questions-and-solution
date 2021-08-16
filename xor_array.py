def xorarr(a,q):
    p,l=0,[]
    for i in range(n):  
        p^=a[i]
        l.append(p)
    print(l)
    for i in q:
        if i[0]==0:
            print(l[i[1]])
        else:
            print(l[i[1]]^l[i[0]-1])

n=int(input())
a=list(map(int, input().split()))
q=int(input())
q1=[]
for i in range(q):
    q1.append(list(map(int,input().split())))

xorarr(a, q1)
