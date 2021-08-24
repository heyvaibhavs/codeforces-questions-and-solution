i=k=0
while k<200:
    x=i
    c=0
    while x>0:
        c+=x%10
        x=x//10
    if c==10:
        k+=1
        print(k,i)
    i+=1
print(k,i)