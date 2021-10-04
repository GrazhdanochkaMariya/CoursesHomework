"""Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает
 её элементы относительно горизонтальной оси симметрии."""

n = int(input())
matrix = [[int(j) for j in input().split()] for _ in range(n)]

matrix.reverse()

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
