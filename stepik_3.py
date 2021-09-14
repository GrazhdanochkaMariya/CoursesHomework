n, m = int(input()), int(input())
matrix = [input().split() for _ in range(n)]

change = input().split()

for r in range(n):
    for c in range(m):
        if c == int(change[0]):
            print(str(matrix[r][int(change[1])]), end=' ')
        elif c == int(change[1]):
            print(str(matrix[r][int(change[0])]), end=' ')
        else:
            print(str(matrix[r][c]), end=' ')
    print()
