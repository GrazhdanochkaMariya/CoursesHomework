n, m = int(input()), int(input())

matrix = []

for i in range(n):
    new_list = []
    for k in range(m):
        new_list.append(i * k)
    matrix.append(new_list)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
