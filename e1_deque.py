from sys import stdin, stdout
from collections import deque, Counter

n1, n2, n3 = stdin.readline().strip().split(" ")
n1, n2, n3 = [int(n1), int(n2), int(n3)]

h1, h2, h3 = deque(), deque(), deque()

h1 = map(int, stdin.readline().strip().split(" "))
h2 = map(int, stdin.readline().strip().split(" "))
h3 = map(int, stdin.readline().strip().split(" "))

h1_sum, h2_sum, h3_sum = deque(), deque(), deque()
c = deque();
"""h1_sum.append(sum(h1))
h2_sum.append(sum(h2))
h3_sum.append(sum(h3))"""

c.append(sum(h1))
c.append(sum(h2))
c.append(sum(h3))

sum1, sum2, sum3 = int(c[0]), int(c[1]), int(c[2])
len1, len2, len3 = n1, n2, n3

count1, count2, count3 = 0, 0, 0

maxlen = max(len1, len2, len3)

if sum1 == sum2 == sum3:
    print sum1
else:
    for i in xrange(0, maxlen):
        if count1 < len1:
            sum1 -= h1[i]
            #h1_sum.append(sum1)
            c.append(sum1)
            count1 += 1
        if count2 < len2:
            sum2 -= h2[i]
            #h2_sum.append(sum2)
            c.append(sum2)
            count2 += 1
        if count3 < len3:
            sum3 -= h3[i]
            #h3_sum.append(sum3)
            c.append(sum3)
            count3 += 1

        #l = list(set(h1_sum) & set(h2_sum) & set(h3_sum))
        q = Counter(c)

        #print (q.most_common(1)[0][1])
        if q.most_common(1)[0][1] == 3:
            print q.most_common(1)[0][0]
            break

