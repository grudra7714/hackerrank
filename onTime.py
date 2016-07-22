#!/bin/python

import sys

yes_or_no = []
t = int(raw_input().strip())
final = []
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    yes_or_no = ["TRUE" for i in xrange(0,len(a)) if a[i] <= 0]
#    print yes_or_no
    if len(yes_or_no) >= k:
        final.append("NO")
    else:
        final.append("YES")

for a0 in xrange(0, len(final)):
    print final[a0]
