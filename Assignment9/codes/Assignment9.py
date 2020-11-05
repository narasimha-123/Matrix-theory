from scipy.linalg import hilbert
import numpy as np

#form a 3x3 Hilbert matrix:
A=hilbert(3)
Ainv=np.linalg.inv(A)
print("A = \n",A)
print("\nA inverse = \n", Ainv)
