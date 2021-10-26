def freq(arr):
    d=dict()
    for i in arr:
        d[i]=d.get(i,0)+1
    return d

for _ in range(int(input())):
    n=int(input())
    a=[]
    a.append(list(map(int, input().split())))
    i=0
    while True:
        d=freq(a[i])
        x=[]
        for j in a[i]:
            x.append(d[j])
        a.append(x)
        if a[-1]==a[-2]:
            break
        i+=1
    z=len(a)-1
    q=int(input())
    for q1 in range(q):
        x,k=map(int, input().split())
        if k>=z:
            print(a[z][x-1])
        else:
            print(a[k][x-1])

    