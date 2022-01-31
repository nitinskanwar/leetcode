memoizeTable = {}
def findOneVal(row, column):
    if column == 0 or row == column:
        memoizeTable[(row, column)] = 1
        return 1
    else:
        if (row, column) not in memoizeTable.keys():
            memoizeTable[(row, column)] = findOneVal(row-1, column-1) + findOneVal(row-1, column)
        return memoizeTable[(row, column)]

def getRow(rowIndex):
    arr = []
    for j in range(rowIndex+1):
        arr.append((findOneVal(rowIndex, j)))
                
    return arr

print(getRow(34));
# print(memoizeTable)