"""Напишите программу, которая поворачивает квадратную матрицу чисел на 90 градусов по часовой стрелке."""

n = int(input())
matrix = [[int(j) for j in input().split()] for _ in range(n)]

matrix.reverse()

for r in range(n):
    for c in range(n):
        print(matrix[c][r], end=' ')
    print()
