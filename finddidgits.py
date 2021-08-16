import math

def is_smart_number(num):
    val =int(num/2)
    c=1
    for i in range (1,val+1):
        if num %i == 0:
            c=c+1
        
    if c%2==0:
        return False
    else:
        return True
            
      

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")



