class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def str(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, other):
        return Matrix([
            [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
            for row_1, row_2 in zip(self.matrix, other.matrix)])


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[5, 2, 1], [4, 9, 6], [7, 4, 9]])
print((m_1 + m_2).str())
