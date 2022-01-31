# This questions involves finding the value at a given location in a pascals triangle. Pascal's triangle is formed as rows and columns with every row 
# having its first and last column value 1. This can be solved using recursion. 

def pascals_triangle(row, column):
    if column == row or column == 1 :
        return 1
    
    return pascals_triangle(row-1, column-1) + pascals_triangle(row-1, column)


print(pascals_triangle(5,3))
print(pascals_triangle(5,2))