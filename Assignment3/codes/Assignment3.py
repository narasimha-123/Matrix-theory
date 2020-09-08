
import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #refered from G.V.V sir's code

#finding solution of two linear equation, this will give the foot of the perpendicular
A = np.array([[4, -3], [3, -5]])
B = np.array([[3], [7]])
S=  np.linalg.inv(A) @ B
print(S)  #this line prints the solution 

#Plotting for showing the graph :

#Inputs
M = np.array([3,3]) #a point satisfying equation1
N = np.array([-3,-5])  # another point satisfying equation1
O = np.array([4,1]) #a point satisfying equation2
P = np.array([-5,-22/5]) #another point satisfying equation2
#Generating all lines
x_AB = line_gen(M,N)
x_CD = line_gen(O,P)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')

plt.plot(M[0], M[1], 'o')
plt.plot(N[0], N[1], 'o')
plt.plot(O[0], O[1], 'o')
plt.plot(P[0], P[1], 'o')
plt.plot(S[0], S[1], 'o')
plt.annotate("Solution (-6/11,-19/11)", (S[0], S[1]))

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

plt.show()

