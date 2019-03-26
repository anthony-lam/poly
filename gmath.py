import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt(vector[0]*vector[0] + vector[1]*vector[1] + vector[2]*vector[2]
	vector[0] /= magnitude
	vector[1] /= magnitude
	vector[2] /= magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return 0

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    return None
