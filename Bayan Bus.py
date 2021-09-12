# problem name : Bayan Bus
# problem link : https://codeforces.com/problemset/problem/475/A
# Rating : 1100

def pattern(n,n1,x,z):
    i=0
    while i <n1:
        if i==0 or i==23 or i==25:
            print("|",end="")
        elif i==26:
            print(")")
        elif i==24:
            if z==1:
                print("D",end="")
            else:
                print(".",end="")
        elif i==1 and x<=n:
            print("O.",end="")
            i+=1
            if x==4:
                x+=3
            else:
                x+=4
        elif x<=n:
            print("O.",end="")
            x+=3
            i+=1
        else:
            print("#.",end="")
            i+=1
        i+=1
        

n=int(input())
for i in range(26):
    if i==0 or i==25:
        print("+",end="")
    else:
        print("-",end="")
print()
pattern(n, 27,1,1)
pattern(n, 26,2,0)
print()
i=0
while i <26:
    if i==1 :
        if n>=3:
            print("O.",end="")
            i+=1
        else:
            print("#.",end="")
            i+=1
    elif i==0 or i==25:
        print("|",end="")
    else:
        print(".",end="")
    i+=1
print()
pattern(n, 27, 4,0)
for i in range(26):
    if i==0 or i==25:
        print("+",end="")
    else:
        print("-",end="")
