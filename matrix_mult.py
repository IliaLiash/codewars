import numpy as np

def matrix_mult(a, b):
    a = np.array(a)
    b = np.array(b)
    return a.dot(b).tolist()
