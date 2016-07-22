import sys

n = int(raw_input().strip())
a = []

for a_i in xrange(n):
    temp = map(int, raw_input().strip().split(' '))
    a.append(temp)

print a
i = 0
front = 0
back = len(a) - 1
front_sum = 0
back_sum = 0

for l in a:
    front_sum += l[front]
    back_sum += l[back]

    front += 1
    back -= 1

print front_sum - back_sum
