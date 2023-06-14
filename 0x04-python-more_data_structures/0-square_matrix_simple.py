#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    mat = []
    for i in matrix:
        mat.append(list(map(lambda x: x**2, i)))
    return mat
