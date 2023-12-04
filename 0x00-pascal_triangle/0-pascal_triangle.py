#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer

"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n"""
   
    pascalArray = []
    if n <= 0:
        return pascalArray
    pascalArray = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(pascalArray[i - 1]) - 1):
            currunt = pascalArray[i - 1]
            temp.append(pascalArray[i - 1][j] + pascalArray[i - 1][j + 1])
        temp.append(1)
        pascalArray.append(temp)
    return pascalArray
