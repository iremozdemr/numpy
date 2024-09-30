import numpy as np

#-5*x0 + 1*x1 = 12
#5*x0 + 3*x1 = 16

a = np.array([[-5,1],[5,3]])
b = np.array([12,16])

number = np.linalg.solve(a,b)

print(number)