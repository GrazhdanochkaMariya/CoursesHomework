"""На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки,
 которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь,
  отметьте символами *, остальные клетки заполните точками."""

n = input()
matrix = [['.'] * 8 for _ in range(8)]

alphabet = 'abcdefgh'

k = alphabet.find(n[0])

for i in range(8):
    for j in range(8):
        if j == k and i == int(n[1]) - 1:
            matrix[i][j] = 'n'
        if i == (int(n[1]) - 1 - 2):
            if j == k - 1 or j == (k + 1):
                matrix[i][j] = '*'
        elif i == (int(n[1]) - 1 - 1):
            if j == (k - 2) or j == (k + 2):
                matrix[i][j] = '*'
        elif i == (int(n[1]) - 1 + 1):
            if j == (k - 2) or j == (k + 2):
                matrix[i][j] = '*'
        elif i == (int(n[1]) - 1 + 2):
            if j == (k + 1) or j == (k - 1):
                matrix[i][j] = '*'
for r in range(7, -1, -1):
    for c in range(8):
        print(matrix[r][c], end=' ')
    print()
