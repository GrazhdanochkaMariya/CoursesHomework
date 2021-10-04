"""Магическим квадратом порядка n называется квадратная таблица размера n×n, составленная из всех чисел
1,2,3,…,n2 так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом."""
n = int(input())
matrix = [[int(j) for j in input().split()] for _ in range(n)]

main = []
side = []
total = sum(matrix[0])
flag = True

num_str = []
for k in range(n ** 2):
    num_str.append(n ** 2 - k)

for i in range(n):
    if sum(matrix[i]) != total:
        flag = False
        break
    for j in range(n):
        if matrix[i][j] not in num_str:
            flag = False
            break
        elif matrix[i][j] in num_str:
            num_str.remove(matrix[i][j])
        if i == j:
            main.append(matrix[i][j])
        if i + j + 1 == n:
            side.append(matrix[i][j])

if flag is True and sum(main) == sum(side) and num_str == []:
    print('YES')
else:
    print('NO')
