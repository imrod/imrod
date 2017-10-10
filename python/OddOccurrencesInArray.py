#!/usr/bin/python


def solution(B):
    freq = {}

    for num in B:
#        print "num = %d" % num
        if num not in freq:
            freq[num] = 1
        elif freq[num] == 2:
            freq[num] = 1
        else:
            freq[num] += 1

    for k, v in freq.iteritems():
        if v == 1:
            return k

if __name__ == '__main__':
    A = [1, 1, 2, 3, 4, 4, 3, 2, 2]
    sol = solution(A)
    print "value is %d" % sol
