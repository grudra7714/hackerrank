#!/bin/python

from sys import stdin, stdout

n1, n2, n3 = stdin.readline().strip().split(" ")
n1, n2, n3 = [int(n1), int(n2), int(n3)]

h1 = map(int, stdin.readline().strip().split(" "))
h2 = map(int, stdin.readline().strip().split(" "))
h3 = map(int, stdin.readline().strip().split(" "))

h1_sum, h2_sum, h3_sum = [sum(h1)], [sum(h2)], [sum(h3)]

sum1, sum2, sum3 = h1_sum[0], h2_sum[0], h3_sum[0]
len1, len2, len3 = n1, n2, n3

count1, count2, count3 = 0, 0, 0

maxlen = max(len1, len2, len3)
#maximum = list(set(list(set(h1_sum).intersection(h2_sum))).intersection(h3_sum))
#if len(maximum) != 0:
#    print maximum[0]
if sum1 == sum2 == sum3:
    print sum1
else:
    for i in xrange(0, maxlen):
        if count1 < len1:
            sum1 -= h1[i]
            h1_sum += [sum1]
            count1 += 1
        if count2 < len2:
            sum2 -= h2[i]
            h2_sum += [sum2]
            count2 += 1
        if count3 < len3:
            sum3 -= h3[i]
            h3_sum += [sum3]
            count3 += 1

        l = list(set(h1_sum) & set(h2_sum) & set(h3_sum))
        if len(l) != 0:
            print l[0]
            break

