"""Программа должна вывести указанную матрицу в соответствии с образцом: разместить единицы на главной и
 побочной диагоналях, остальные позиции матрицы заполнить нулями."""

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = 1
    matrix[i][n - i - 1] = 1

for r in range(n):
    for c in range(n):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
