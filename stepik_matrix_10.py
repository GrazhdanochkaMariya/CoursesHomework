"""На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n×m,
 заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка.
 Выведите полученную матрицу на экран, разделяя элементы пробелами."""

x = input().split()
n = int(x[0])
m = int(x[1])
matrix = [['.'] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
            matrix[i][j] = '*'

for k in range(n):
    for o in range(m):
        print(matrix[k][o], end=' ')
    print()
