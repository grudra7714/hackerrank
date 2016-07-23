# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter, deque
from sys import stdin, stdout

import time

with open("input_4") as f:
    content = f.readlines()
    n1, n2, n3 = content[0].strip().split(" ")
    n1, n2, n3 = int(n1), int(n2), int(n3)
    a1 = map(int, content[1].split(" "))
    a2 = map(int, content[2].split(" "))
    a3 = map(int, content[3].strip().split(" "))

start = time.clock()

a1.reverse()
a2.reverse()
a3.reverse()


x = dict()
s = 0
x[0] = 3
for i in xrange(n1):
    s += a1[i]
    if s in x:
        x[s] += 1
    else:
        x[s] = 1
s = 0
for i in xrange(n2):
    s += a2[i]
    if s in x:
        x[s] += 1

mx = 0

s = 0
for i in xrange(n3):
    s += a3[i]
    if s in x:
        x[s] += 1
        if x[s] == 3:
            mx = max(mx, s)

print(mx)

print (time.clock() - start)