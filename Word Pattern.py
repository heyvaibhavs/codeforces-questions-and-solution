# problem name : Word Pattern
# problem link : https://leetcode.com/problems/word-pattern/
# level : medium
from ordered_set import OrderedSet
def wordpattern(p,s):
    l1=list(p)
    l2=list(s.split(" "))
    k=0
    for i in l1:
        for j in range(len(l1)):
            if l1[j]==i:
                l1[j]=k
        k+=1
    k=0
    for i in l2:
        for j in range(len(l2)):
            if l2[j]==i:
                l2[j]=k
        k+=1
    if l1==l2:
        return True
    return False
        
print(wordpattern('papa', "cat dog cat dog"))