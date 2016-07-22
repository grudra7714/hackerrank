#!/bin/python

import sys


time = raw_input().strip()
arr = time.split(":")

hour = arr[0]
hour = int(hour)

time = arr[2][2:]

if time == "PM" or time == "pm":
    if(hour < 12):
        hour += 12

if time =="AM" or time == "am":
    if(hour == 12):
        hour = str(hour)
        hour = "00"
    if(hour < 10):
        hour = str(hour)
        hour = "0" + hour

print str(hour)+":"+str(arr[1])+":" + str(arr[2][:2])