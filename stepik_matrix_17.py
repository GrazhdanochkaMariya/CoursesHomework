"""На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером
n×m заполнив её "змейкой" в соответствии с образцом."""

x = input().split()
y = [int(i) for i in x]

matrix = [[j for j in range(k * y[1] + 1, k * y[1] + y[1] + 1)] for k in range(y[0])]

for m in range(y[0]):
    if m % 2 == 1:
        matrix[m].reverse()

for r in range(y[0]):
    for c in range(y[1]):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
