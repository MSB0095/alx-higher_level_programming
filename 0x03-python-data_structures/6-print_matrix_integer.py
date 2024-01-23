#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    if matrix:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if j < (len(matrix[i]) - 1):
                    print("{:d}".format(int(matrix[i][j])), end=' ')
                elif j == (len(matrix[i]) - 1):
                    print("{:d}".format(int(matrix[i][j])))
