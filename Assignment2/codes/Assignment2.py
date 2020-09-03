#Code by GVV Sharma
#November 19, 2019
#released under GNU GPL
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

import math
vector_1 = [3,2,6] #Direction vector of first line in problem 1
vector_2 = [1,2,2] #Direction vector of second line in problem 1
vector_3 = [1,-1,-2] #Direction vector of first line in problem 2
vector_4 = [3,-5,-4] #Direction vector of second line in problem 2

unit_vector_1 = vector_1 / np.linalg.norm(vector_1) #Calculating unit vector of vector1
unit_vector_2 = vector_2 / np.linalg.norm(vector_2) #Calculating unit vector of vector2
unit_vector_3 = vector_3 / np.linalg.norm(vector_3) #Calculating unit vector of vector3
unit_vector_4 = vector_4 / np.linalg.norm(vector_4) #Calculating unit vector of vector4
dot_product1 = np.dot(unit_vector_1, unit_vector_2) #calculating dot product of unit vector 1 and 2
dot_product2 = np.dot(unit_vector_3, unit_vector_4) #calculating dot product of unit vector 3 and 4
angle1 = np.arccos(dot_product1) * 180 / math.pi #calculating angle between of unit vector 1 and 2
angle2 = np.arccos(dot_product2) * 180 / math.pi #calculating angle between of unit vector 3 and 4
print("Problem (1) - Angle between L1 and L2 is : ", angle1)
print("Problem (2) - Angle between L1 and L2 is : ", angle2)

#creating x,y for 3D plotting for problem 1
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
#ax = fig.add_subplot(111,projection='3d',aspect='equal')

#Points on the plane
A = np.array([5,-3,7]).reshape((3,1))
B = np.array([2,-5,1]).reshape((3,1))
C = np.array([8,-4,2]).reshape((3,1))
D = np.array([7,-6,0]).reshape((3,1))


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(C,D)


#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],label="AB")
plt.plot(x_BC[0,:],x_BC[1,:],x_BC[2,:],label="BC")

#plotting point
ax.scatter(A[0],A[1],A[2],'o')
ax.scatter(B[0],B[1],B[2],'o')
ax.scatter(C[0],C[1],C[2],'o')
ax.scatter(D[0],D[1],D[2],'o')

ax.text(5,-3,7, "A", color='red')
ax.text(2,-5,1, "B", color='red')
ax.text(8,-4,2, "C", color='red')
ax.text(7,-6,0, "D", color='red')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()

	#creating x,y for 3D plotting for problem 2
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig1 = plt.figure()
ax = fig1.add_subplot(111,projection='3d')
#ax = fig1.add_subplot(111,projection='3d',aspect='equal')

#Points on the plane
A1 = np.array([7,-3,-10]).reshape((3,1))
B1 = np.array([0,4,4]).reshape((3,1))
C1 = np.array([5,-6,-60]).reshape((3,1))
D1 = np.array([2,-1,-56]).reshape((3,1))


#Generating all lines
x_AB1 = line_gen(A1,B1)
x_BC1 = line_gen(C1,D1)


#plotting line
plt.plot(x_AB1[0,:],x_AB1[1,:],x_AB1[2,:],label="AB")
plt.plot(x_BC1[0,:],x_BC1[1,:],x_BC1[2,:],label="BC")

#plotting point
ax.scatter(A1[0],A1[1],A1[2],'o')
ax.scatter(B1[0],B1[1],B1[2],'o')
ax.scatter(C1[0],C1[1],C1[2],'o')
ax.scatter(D1[0],D1[1],D1[2],'o')

ax.text(7,-3,-10, "A", color='red')
ax.text(0,4,4, "B", color='red')
ax.text(5,-6,-60, "C", color='red')
ax.text(2,-1,-56, "D", color='red')

#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()

	





