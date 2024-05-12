import numpy as np
import time
import sys

l = range(1000)
print('lenght is', len(l))
print(sys.getsizeof(5))
print(sys.getsizeof(5)*len(l))
array = np.arange(1000)
print(len(array))
print(array.size*array.itemsize)

l1 = range(1000000)
l2 = range(1000000)

a1 = np.arange(1000000)
a2 = np.arange(1000000)

print(zip(l1, l2))

start = time.time()
result = [(x+y) for x, y in zip(l1, l2)]
print("it took: ", (time.time()-start)*1000)

start = time.time()
result = a1+a2

print('numpy took: ', (time.time()-start)*1000)

a1 = np.array([1, 2, 3])
a2 = np.array([1, 2, 3])

print(a1+a2)

a = np.array([1.5, 2.5, 3.5])
print(a.itemsize)

a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
b = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2], [9, 3, 2]])

print(a[:, 1:])
print(np.hstack((a, b)))
