s="1011"
x=s[0]
y=1
i=1

while i!=len(s):
    z=""
    c=0
    for j in range(i,i+y):
        z=z+s[j]
    if int(x)+1==int(z):
        x=z
        i+=y
        c=1
       
    else:
        x=""
        for j in range(0,i+y):
            x=x+s[j]
        y+=i
        i+=1
if i==len(s):
    if c==1:
        print("YES")
        
    else:
        print("NO")
        
        
    
        