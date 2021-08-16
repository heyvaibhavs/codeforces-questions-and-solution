def count(num):
    y=0
    c=0
    for i in range(2,num+1):
        for j in range(1,int(i/2+1)):
            if(i%j==0):
                c=1
                break
        if(c==0):
            y+=1
        return y
print(count(2000))    