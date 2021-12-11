# Code by : Sam._.072

n = int(input())
print(n,end=" ")
x = n//2
# print(x,n)
while x > 0:
    while x > 0 and n%x != 0:
        x -= 1
    print(x,end=" ")
    n = x
    x = x//2
    # print(x,n)
    