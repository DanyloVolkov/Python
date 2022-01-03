class Matrix:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join(str(i) for i in self.data)

    def __add__(self, other):
        data = []

        for j in range(len(self.data)):
            data.append([])
            for k in range(len(self.data[0])):
                data[j].append(self.data[j][k] + other.data[j][k])

        return Matrix(data)

matrix_3_2 = Matrix([[1,2], [1,2,], [1,2]])
matrix_3_2 = Matrix([[1,2], [1,2,], [1,2]])
matrix_3_3 = Matrix([[1,2,3], [1,2,3], [1,2,3]])
matrix_3_3 = Matrix([[1,2,3], [1,2,3], [1,2,3]])
matrix_4_4 = Matrix([[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]])
matrix_4_4 = Matrix([[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4]])

print(matrix_3_2, '\n')
print(matrix_3_3, '\n')
print(matrix_4_4, '\n')

print(matrix_3_2 + matrix_3_2, '\n')
print(matrix_3_3 + matrix_3_3, '\n')
print(matrix_4_4 + matrix_4_4, '\n')