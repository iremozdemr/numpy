#numpy array'i oluşturma:

import numpy as np

array = np.array([1,2,3,4,5])
print(type(array))
print(array)

array = np.zeros(10)
print(type(array[0]))
print(array)
#10 tane float tipinde 0 içeren array
#çıktı: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

array = np.zeros(10,dtype=float)
print(type(array[0]))
print(array)
#10 tane float tipinde 0 içeren array
#çıktı: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

array = np.zeros(10,dtype=int)
print(type(array[0]))
print(array)
#10 tane int tipinde 0 içeren array
#çıktı: [0 0 0 0 0 0 0 0 0 0] 

array = np.zeros(10,dtype=str)
print(type(array[0]))
print(array)
#10 tane str tipinde 0 içeren array
#çıktı: ['' '' '' '' '' '' '' '' '' '']

random_number = np.random.randint(0,10)
print(type(random_number))
print(random_number)
#0-10 arasında random bir sayı üretir

random_array = np.random.randint(0,10,5)
print(type(random_array))
print(random_array)
#0-10 arasında 5 tane random sayı içeren array üretir

my_array = np.random.normal(10,4,(2,3))
print(type(my_array))
print(my_array)
#ortalaması = 10
#standart sapması = 4
#boyutu = 2x3
#array oluşturma