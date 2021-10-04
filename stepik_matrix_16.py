"""На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером
n×m заполнив её в соответствии с образцом."""

x = input().split()
int_x = [int(i) for i in x]

matrix = [[((k + j) % int_x[1]) + 1 for j in range(int_x[1])] for k in range(int_x[0])]

for r in range(int_x[0]):
    for c in range(int_x[1]):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
