#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): which returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    answer = []
    if n > 0:
        for i in range(1, n + 1):
            stage = []
            C = 1
            for j in range(1, i + 1):
                stage.append(C)
                C = C * (i - j) // j
            answer.append(stage)
    return answer
