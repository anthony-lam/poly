import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
	print(vector)
	magnitude = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2])
	if (not magnitude == 0):
		vector[0] /= magnitude
		vector[1] /= magnitude
		vector[2] /= magnitude
	print (vector)


#Return the dot porduct of a . b
def dot_product(a, b):
	prod = 0
	for i in range(len(a)):
	    prod = prod + a[i] + b[i]
	return prod
	

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygon, i):
    a = [polygon[i+1][0] - polygon[i][0], polygon[i+1][1] - polygon[i][1], polygon[i+1][2] - polygon[i][2]]
    b = [polygon[i+2][0] - polygon[i][0], polygon[i+2][1] - polygon[i][1], polygon[i+2][2] - polygon[i][2]]
    prod = [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]* b[1] - a[1]*b[0]]
    return  prod[2]
