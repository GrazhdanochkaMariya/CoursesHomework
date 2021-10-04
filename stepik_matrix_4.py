"""Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали."""

n = int(input())
matrix = [input().split() for _ in range(n)]
flag = True

for i in range(n):
    if not flag:
        break
    for j in range(n):
        if i != j:
            if matrix[i][j] != matrix[j][i]:
                flag = False
                break

if flag:
    print('YES')
else:
    print('NO')