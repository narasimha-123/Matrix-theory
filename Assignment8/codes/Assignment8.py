# Python program to find the Perpendicular(shortest) 
# distance between a point and a Plane in 3 D. 
  
import math 
  
# Function to find distance 
def shortest_distance(x1, y1, z1, a, b, c, d):  
      
    d = abs((a * x1 + b * y1 + c * z1 + d))  
    e = (math.sqrt(a * a + b * b + c * c)) 
    return (d/e)
    
      
  
# Point
x1 = -1
y1 = 2
z1 = -4

#plane parameters
a = 3
b = 2
c = -6
d = -2
  
# Function call 
d=shortest_distance(x1, y1, z1, a, b, c, d)   
print("The distance between the point and plane is", d)