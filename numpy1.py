import numpy as np

#numpy kullanmadan:

a = [1,2,3,4,5]
b = [2,3,4,5,6]

ab = []

for index in range(0,len(a)):
    ab.append(a[index] * b[index])

print(ab)

#numpy kullanarak:

a = np.array([1,2,3,4,5])
b = np.array([2,3,4,5,6])

print(a*b)