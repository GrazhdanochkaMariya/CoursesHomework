"""На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n×m
заполнив её "диагоналями" в соответствии с образцом."""

n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
x = 0

for i in range(n + m):
    if i <= m:
        if i < n:
            for j in range(n - (n - i)):
                x += 1
                matrix[j][i - 1 - j] = x
        if i >= n:
            for q in range(n):
                x += 1
                matrix[q][i - 1 - q] = x
    if i > m:
        if n + m - i < m:
            for k in range(n + m - i):
                x += 1
                matrix[i - m + k][m - 1 - k] = x
        elif n + m - i >= m:
            for q in range(m):
                x += 1
                matrix[i - m + q][m - 1 - q] = x

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
