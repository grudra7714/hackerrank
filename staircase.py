import sys

n = int(raw_input().strip())
count = 1
size = n + 1

for i in reversed(range((n+1))):
    print " " * size + "#" * count
    count +=1
    size -=1