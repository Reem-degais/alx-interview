#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n: int) -> int:
    """ Minimum Operations needed to get n H characters """
    next = 'H'
    body = 'H'
    operation = 0
    while (len(body) < n):
        if n % len(body) == 0:
            operation += 2
            next = body
            body += body
        else:
            operation += 1
            body += next
    if len(body) != n:
        return 0
    return operation
