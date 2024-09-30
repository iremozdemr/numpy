import numpy as np

a = np.random.randint(0,10,size=10)

print(a)
print(a[0])
print(a[9])
print(a[-1])
print(a[0:5])

b = np.random.randint(0,10,size=10)
print(b)

b[0] = 12
print(b)
#b[0] = 12 olur

b[1] = 2.7
print(b)
#b[1] = 2 olur

x = np.random.randint(0,10,size=(3,5))

print(x)

print(x[0,0])
print(x[0,1])
print(x[0,2])

print(x[0])
print(x[0,:])
print(x[1])
print(x[1,:])
print(x[2])
print(x[2,:])

print(x[:,0])
print(x[:,1])
print(x[:,2])
print(x[:,3])
print(x[:,4])