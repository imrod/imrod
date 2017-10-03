def FirstFactorial(num):
    num = int(num)
    # code goes here
    for i in range(num - 1, 0, -1):
        num = num * i
    return num


# keep this function call here
print FirstFactorial(raw_input())

