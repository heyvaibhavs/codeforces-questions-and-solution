# Code by : Sam._.072

def conversion(n, b):
    s=''
    while n>=b:
        s+=str(n%b)
        n=n//b
        
    s+=str(n)
    return s[::-1]

print(conversion(31, 8))