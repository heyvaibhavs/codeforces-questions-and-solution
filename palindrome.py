#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    c=0
    h='0'
    j=n-1
    for i in range(n//2):
        if s[i]!=s[j]:
            c=c+1
            if s[i]>s[j] and s[i]>h:
                h=s[i]
            elif s[j]>s[i] and s[j]>h:
                h=s[j]
            else:
                h=h
        j=j-1
    if k+1==c*2:
        j=n-1
        s1=""
        l=list(s)
        for i in range(n//2):
            if l[i]!=l[j]:
                l[i]=h
                l[j]=h
            j=j-1
        return s1.join(l)
    elif c==0:
        return s
    else:
        return "-1"


    


   



nk = input()
n=int(nk[0])
k=int(nk[1])

s = input()

print(highestValuePalindrome(s, n, k))

 
