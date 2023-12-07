#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append((matrix[i][j])**2)
        new_mat.append(row)
    return new_mat
