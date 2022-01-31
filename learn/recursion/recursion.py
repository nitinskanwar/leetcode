def reverseStringRecursive(stringToReverse):
    if len(stringToReverse) == 1:
        return stringToReverse
    return reverseStringRecursive(stringToReverse[1:]) + stringToReverse[0]

# This function will not work because strings are immutable and we can't change specific values in a string
def reverseStringIterative(stringToReverse):
    if len(stringToReverse) == 1:
        return stringToReverse
    front = 0
    end = len(stringToReverse)-1
    while front <= end:
        temp = stringToReverse[front]
        stringToReverse[front] = stringToReverse[end]
        stringToReverse[end] = temp
        front += 1
        end -= 1
    return stringToReverse

def printReversedString(stringToReverse):
    print(reverseStringRecursive(stringToReverse))
    print(reverseStringIterative(stringToReverse))

printReversedString('Nitin Kanwar')