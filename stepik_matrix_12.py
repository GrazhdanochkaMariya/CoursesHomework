"""На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу размером
n×m и заполняет её числами от 1 до n⋅m в соответствии с образцом."""

x = input().split()
int_x = [int(i) for i in x]

matrix = [[j for j in range(k * int_x[1] + 1, k * int_x[1] + int_x[1] + 1)] for k in range(int_x[0])]

for row in range(int_x[0]):
    for clmn in range(int_x[1]):
        print(str(matrix[row][clmn]).ljust(3), end='')
    print()
