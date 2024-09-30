import numpy as np

array1 = np.array([1,2,3,4,5])

new_array = array1 / 5
print(new_array)

new_array = array1 * 2
print(new_array)

array2 = np.array([1,2,3,4,5])

num1 = np.subtract(array2,4)
print(num1)

num2 = np.add(array2,4)
print(num2)

num3 = np.mean(array2)
print(num3)

num4 = np.sum(array2)
print(num4)

num5 = np.min(array2)
print(num5)

num6 = np.max(array2)
print(num6)

num7 = np.var(array2)
print(num7)