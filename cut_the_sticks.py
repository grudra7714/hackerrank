#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

count = 0
repeat = True
l1 = []
while repeat:
    m = min(arr)
    l = len(arr)
    arr = list(map(lambda x: x - m, arr))
    l1.append(len(arr))
    arr = filter(lambda a: a != 0, arr)
    print arr
    if len(arr) == 0:
        print '\n'.join(map(str, l1))
        repeat = False