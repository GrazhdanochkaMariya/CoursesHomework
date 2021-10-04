"""На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером n×m
 заполнив её "спиралью" в соответствии с образцом."""

q, w = map(int, input().split())
n = q
m = w
matrix = [[0] * w for _ in range(q)]
x = 1
count = 0

while x <= q * w:
    for i in range(m - 1):
        matrix[count][i + count] = x
        x += 1
    for j in range(n - 1):
        matrix[j + count][m - 1 + count] = x
        x += 1
    for k in range(m - 1):
        matrix[n - 1 + count][m - 1 + count - k] = x
        x += 1
    for z in range(n - 1):
        matrix[n - 1 + count - z][count] = x
        x += 1

    count += 1
    n -= 2
    m -= 2

for r in range(q):
    for c in range(w):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
