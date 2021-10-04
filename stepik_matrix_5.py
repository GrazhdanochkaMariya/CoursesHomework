"""Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы,
 стоящие на главной и побочной диагонали, при этом каждый элемент должен остаться в том же столбце
 (то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали)."""

n = int(input())
matrix = [[int(j) for j in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j], matrix[n-i-1][i] = matrix[n-i-1][i], matrix[i][j]

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()