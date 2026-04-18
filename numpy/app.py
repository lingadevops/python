import numpy as np
#array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#print(array)
#print(array.shape)

array = np.zeros((3, 3), dtype=int)
array = np.random.random((3, 4))
print(array)

print(array[0, 0])
print(array[0, :])
print(array > 0.5)

print(np.sum(array))
print(np.mean(array))

#mean formula: mean = sum of values / number of values

array = [1, 2, 3]

new_array = [x * 2 for x in array]

print(new_array)
