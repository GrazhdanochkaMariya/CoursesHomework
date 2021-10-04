"""На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером
 n×n заполнив её в соответствии с образцом."""
from math import ceil

n = int(input())
matrix = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i < ceil((n - 1) / 2):
            if j < i or j > (n - i - 1):
                matrix[i][j] = 0
        if i >= ceil((n - 1) / 2):
            if j > i or j < (n - i - 1):
                matrix[i][j] = 0

for r in range(n):
    for c in range(n):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
