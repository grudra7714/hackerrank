#!/bin/python

from __future__ import division
import sys

a = []
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print a

size = len(a)
pos,neg,neu = 0,0,0

for num in a:
    if num > 0: pos += 1
    if num < 0: neg += 1
    if num == 0: neu += 1

pos = float(pos)
neg = float(neg)
neu = float(neu)

print "%0.6f"%(pos/size)
print "%0.6f"%(neg/size)
print "%0.6f"%(neu/size)

