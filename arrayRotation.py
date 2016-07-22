# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    from sys import stdin, stdout
    from collections import deque

    # l = map(int, raw_input().strip().split(' '))
    n, k, q = stdin.readline().strip().split(" ")
    n = int(n)
    k = int(k)
    q = int(q)

    num = map(int, stdin.readline().strip().split(" "))
    d = deque(num)
    d.rotate(k)

    # print "Final num: %s"%(num)
    final = []
    # final = map(int, stdin.readline().strip())
    for i in xrange(0, q):
        pos = int(raw_input().strip())
        final.append(d[pos])

    for i in xrange(0, len(final)):
        print final[i]


if __name__ == "__main__":
    main()