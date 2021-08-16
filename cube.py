def count(name):
    num={}
    for i in name:
        num[i]=name.count(i)
    return num
n=input("enter a number")
print(count(n))