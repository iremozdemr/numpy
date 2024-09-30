import numpy as np

#ndim: boyut sayısı
#shape: boyut bilgisi
#size: toplam eleman sayısı
#dtype: array veri tipi

array = np.random.randint(0,10,size=5)
print(array)
#0-10 arasında 5 tane random sayı içeren array üretir

array = np.random.randint(10,size=5)
print(array)
#0-10 arasında 5 tane random sayı içeren array üretir

a = np.random.randint(0,10,size=5)

print(a.ndim)
#çıktı: 1
print(a.shape)
#çıktı: (5,)
print(a.size)
#çıktı: 5
print(a.dtype)
#çıktı: int64

b = np.random.randint(0,10,size=3)

print(b.dtype)
#çıktı: int64

print(type(b))
#çıktı: <class 'numpy.ndarray'>