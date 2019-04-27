import numpy as np

def pool(m, f, I, J):
    rows = list()
    for i in range(0, m.shape[0] - I + 1, I):
        cols = list()
        for j in range(0, m.shape[1] - J + 1, J):
            cols.append(f(m[i:(i+I),j:(j+J)]))
        rows.append(cols)
    return(np.matrix(rows))

def matrix_round(m):
    return(np.matrix([[round(x) for x in xs] for xs in m.tolist()]))

def matrix_random(width, height):
    return(np.random.rand(width, height))

def tolist(m):
    return(m.tolist())

def diagonal(m):
    return(m.diagonal())

matrix_add = np.add
matrix_sub = np.subtract
matrix_sum = np.sum
matrix_max = np.max
matrix_min = np.min
scalar_multiply = np.multiply
matrix_multiply = np.matmul
matrix = np.matrix
