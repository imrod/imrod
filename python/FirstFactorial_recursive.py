def FirstFactorial(num):
    num = int(num)
    # code goes here
    if num is 1:
        return 1
    else:
        num = num * FirstFactorial(num - 1)

    print 'num = %s' % num
    return num


# keep this function call here
print FirstFactorial(raw_input())

