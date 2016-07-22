#!/usr/bin/python


# !/bin/python

import sys

n1, n2, n3 = raw_input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
c = [n1, n2, n3]
mini = max(c)
h1 = map(int, raw_input().strip().split(' '))
h2 = map(int, raw_input().strip().split(' '))
h3 = map(int, raw_input().strip().split(' '))


def pop_h1(h1):
    return h1[1:]


def pop_h2(h2):
    return h2[1:]


def pop_h3(h3):
    return h3[1:]


found = False

for i in xrange(0, mini):
    sum_h1, sum_h2, sum_h3 = sum(h1), sum(h2), sum(h3)
    if sum_h1 == sum_h2 == sum_h3:
        print sum_h1
        found = True
        break
    else:
        if sum_h1 == sum_h2 != sum_h3:
            if sum_h1 < sum_h3:
                h_temp = h3
                for j in xrange(0, len(h3)):
                    h3 = pop_h3(h3)
                    h_temp_sum = sum(h3)
                    if sum_h1 == h_temp_sum:
                        print sum_h1
                        found = True
                        break
                    elif sum_h1 > h_temp_sum:
                        break
            else:
                h1, h2 = pop_h1(h1), pop_h2(h2)

        elif sum_h2 == sum_h3 != sum_h1:
            if sum_h2 < sum_h1:
                h_temp = h1
                for k in xrange(0, len(h1)):
                    h1 = pop_h1(h1)
                    h_temp_sum = sum(h1)
                    if sum_h2 == h_temp_sum:
                        print sum_h1
                        found = True
                        break
                    elif sum_h2 > h_temp_sum:
                        break
            else:
                h2, h3 = pop_h1(h2), pop_h2(h3)
        elif sum_h1 == sum_h3 != sum_h2:
            if sum_h1 < sum_h2:
                h_temp = h2
                for l in xrange(0, len(h2)):
                    h2 = pop_h2(h2)
                    h_temp_sum = sum(h2)
                    if sum_h1 == h_temp_sum:
                        print sum_h1
                        found = True
                        break
                    elif sum_h1 > h_temp_sum:
                        break
            else:
                h1, h3 = pop_h1(h1), pop_h2(h3)

        elif sum_h1 != sum_h3 != sum_h2:
            h1, h2, h3 = pop_h1(h1), pop_h2(h2), pop_h3(h3)

        if found:
            break


