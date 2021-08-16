x,y=map(int,input().split())
if (x==2 and y==4) or x==y or (x==4 and y==2):
    print("=")
elif x==1 or y==1:
    if x==1:
        print("<")
    elif y==1:
        print(">")
elif x<y :
    print(">")
else:
    print("<")
