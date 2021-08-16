a,b=map(int,input().split())
l=[b]
while a<b:
    if b%10==1:
        b=b//10
        l.append(b)
    elif (b%10)%2!=0:
        print("NO")
        exit()
    else:
        b=b//2
        l.append(b)
    if b==a:
        print("YES")
        print(len(l))
        l.reverse()
        print(*l)
        exit()

print("NO")

