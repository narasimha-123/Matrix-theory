import numpy as np

V = np.array([[1, 0], [0, -1]])
Q, R=np.linalg.qr(V)
print("Q=",Q)
print("R=",R)