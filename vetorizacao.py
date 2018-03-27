import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import svd

from sympy.matrices import Matrix
from sympy import init_printing
from sympy import latex
import math

init_printing()

def printm(m):
    display(Matrix(m))
    
def printl(m):
    print(latex(Matrix(np.array(m*100, dtype=int)/100)))
    
def gen_rank_k(k, U, W, Vt):
    temp = np.matmul(U[:,:k], np.diag(W[:k]))
    return np.matmul(temp, Vt[:k, :])
