# task1: creating Numpy Arrays
import numpy as np

# CREATE 1D AND 2D ARRRAY
arr_1 = np.arange(1,11)
arr_2 = np.arange(1,10).reshape(3,3)

# numpy array from the list 

list = [1,2,3,4,5,6,7,8,9]
arr_3 = np.array(list)

# for 1d array
print("1D Array:", arr_1)
print("Shape:", arr_1.shape)
print("data type:", arr_1.dtype)

# for 2d array
print("2D Array:\n", arr_2)
print("Shape:", arr_2.shape)
print("data type:", arr_2.dtype)

# for 3d array
print("3D Array:", arr_3)
print("Shape:", arr_3.shape)
print("data type:", arr_3.dtype)

