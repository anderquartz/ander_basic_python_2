matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          ]

print(matrix)
print(matrix[1])
print(matrix[2][0])

matrix[0][0] = 0
matrix[0][1] = 0
matrix[0][2] = 0
matrix[0][3] = 0
matrix[1][3] = 'Python'
print(matrix)