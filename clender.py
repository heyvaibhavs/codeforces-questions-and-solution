s1=input()
s2=input()
if s1==s2:
    print("YES")
else:
    d={"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
    if d[s2]>d[s1]:
        x=d[s2]-d[s1]
    else:
        x=7-d[s1]+d[s2]
    # print(d[s1],d[s2],x)
    if x==2 or x==3:
        print("YES")
    else:
        print("NO")