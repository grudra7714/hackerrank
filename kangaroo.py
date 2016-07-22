#!/bin/python

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

diff = x2 - x1
a = 0
for i in range(0, diff):
    x1 += v1
    x2 += v2
    if(x1 == x2):
        print "YES"
        a = 1
        break

if a != 1:
    print "NO"


