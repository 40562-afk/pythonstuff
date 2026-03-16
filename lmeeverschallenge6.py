import numpy as np

array = np.array([9, 3, 5, 6, 2, 5, 7, 0, 1, 0])
mean = np.mean(array) 
median = np.median(array)
std = np.std(array)
print(mean)
print(median)
print(std)

array_time_2 = array * 2
print(array_time_2)
array_time_2[array_time_2 < 4] = 0
print(array_time_2)