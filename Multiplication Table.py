# Code by : Sam._.072

def dec_to_base(num,base):  #Maximum base - 36
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base

    base_num = base_num[::-1]  #To reverse the string
    return base_num

n = int(input())
for i in range(1,n):
    for j in range(1,n):
        print(dec_to_base(i*j, n),end=" ")
    print()