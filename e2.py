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
d1, d2,d3 = True, True, True
l = []
#maximum = list(set(list(set(h1_sum).intersection(h2_sum))).intersection(h3_sum))
#if len(maximum) != 0:
#    print maximum[0]
if sum1 == sum2 == sum3:
    print sum1
else:
    for i in xrange(0, maxlen):
        if count1 < len1 and d1:
            sum1 -= h1[i]
            h1_sum.append(sum1)
            count1 += 1
        if count2 < len2 and d2:
            sum2 -= h2[i]
            h2_sum.append(sum2)
            count2 += 1
        if count3 < len3 and d3:
            sum3 -= h3[i]
            h3_sum.append(sum3)
            count3 += 1

        if len(list(set(h1_sum).intersection(h2_sum))) != 0:
            l = list(set(h1_sum).intersection(h2_sum))
            if(l[len(l)-1] == sum3):
                print l[len(l)-1]
                break
            elif l[len(l)-1] < sum3:
                d1,d2 = False, False
            else:
                d1,d2 = True, True

        elif len(list(set(h2_sum).intersection(h3_sum))) != 0:
            l = list(set(h2_sum).intersection(h3_sum))
            if (l[len(l)-1] == sum1):
                print l[0]
                break
            elif l[len(l) - 1] < sum1:
                d2, d3 = False, False
            else:
                d2, d3 = True, True

        elif len(list(set(h3_sum).intersection(h1_sum))) != 0:
            l = list(set(h3_sum).intersection(h1_sum))
            if (l[len(l) - 1] == sum2):
                print l[0]
                break

            elif l[len(l) - 1] < sum2:
                d1, d3 = False, False
            else:
                d1, d3 = True, True
