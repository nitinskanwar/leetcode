from decimal import *
def calculatePow(x, n):
    result = 1
    print("1")
    if n < 0:
        k = n * -1
        print(2)
        for i in range(k):
            print("here")
            result *= (1/x)
    else:
        print(3)
        for i in range(n):
            result *= x
    
    return result

print(calculatePow(2.00000,-2))