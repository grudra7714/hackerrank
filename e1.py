#!/bin/python
from collections import Counter, deque
from sys import stdin, stdout

import time

with open("input_4") as f:
    content = f.readlines()
    n1, n2, n3 = content[0].strip().split(" ")
    n1, n2, n3 = int(n1), int(n2), int(n3)
    h1 = map(int, content[1].split(" "))
    h2 = map(int, content[2].split(" "))
    h3 = map(int, content[3].strip().split(" "))

c = {}
h1_sum, h2_sum, h3_sum = [sum(h1)], [sum(h2)], [sum(h3)]
sum1, sum2, sum3 = h1_sum[0], h2_sum[0], h3_sum[0]
len1, len2, len3 = n1, n2, n3
maxlen = max(len1, len2, len3)


start = time.clock()
if sum1 == sum2 == sum3:
    print sum1
else:
    for i in xrange(0, maxlen):
        if i < len1:
            sum1 -= h1[i]
            if not c.has_key(sum1):
                c[sum1] = 1
            else:
                c[sum1] += 1
                if c[sum1] == 3:
                    print sum1
                    break

        if i < len2:
            sum2 -= h2[i]
            if not c.has_key(sum2):
                c[sum2] = 1
            else:
                c[sum2] += 1
                if c[sum2] == 3:
                    print sum2
                    break

        if i < len3:
            sum3 -= h3[i]
            if not c.has_key(sum3):
                c[sum3] = 1
            else:
                c[sum3] += 1
                if c[sum3] == 3:
                    print sum3
                    break

print (time.clock() - start)