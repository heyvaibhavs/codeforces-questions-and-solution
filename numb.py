#!/bin/python3

import math
import os
import random
import re
import sys

p=int(input())
q=int(input())
t=0
k=0
while p<=q:
    t=p
    l="0"
    r="0"
    d=0
    while t!=0:
        d=d+1
        t=t//10
    t=str(p*p)
    if len(t)%2!=0:
        l1=d-1
    else:
        l1=d
    for i in range(l1,len(t)):
        r=r+t[i]
    for i in range(l1):
        l=l+t[i]
    if int(r)+int(l)==p:
        k=-1
        print(p)
    if k==0 and p==q:
        print("INVALID RANGE")
    p=p+1
