import math
def lcm(a):
    ans=1
    for i in a:
        ans=int((ans*i)/math.gcd(ans,i))
    return ans
print(lcm([2,4,3,14,15,6,18]))