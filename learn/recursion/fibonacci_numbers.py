memoizeTable = {}
def fibonacci(num):
    if num < 2:
        memoizeTable[num] = num
        return num
    else:
        if num not in memoizeTable.keys():
            memoizeTable[num] = fibonacci(num-1) + fibonacci(num-2)
        return memoizeTable[num]

print(fibonacci(900))
print(memoizeTable)