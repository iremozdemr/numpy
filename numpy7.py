import numpy as np

#yöntem 1:

array = np.array([1,2,3,4,5])

new_array = []

for number in array:
    if number < 4:
        new_array.append(True)
    else:
        new_array.append(False)

print(new_array)

#yöntem 1:

array = np.array([1,2,3,4,5])

new_array = []

new_array = array < 4

print(new_array)