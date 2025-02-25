import numpy as np

# Creating a 1D NumPy array
array_1d = np.array([1, 2, 3, 4])
print("1D Array:", array_1d)  # Expected Output: 1D Array: [1 2 3 4]

# Creating a 2D NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)
# Expected Output:
# 2D Array:
# [[1 2 3]
#  [4 5 6]]

# Array attributes
print("Shape:", array_2d.shape)  # Expected Output: Shape: (2, 3) - 2 rows and 3 columns
print("Size:", array_2d.size)   # Expected Output: Size: 6 - Total 6 elements
print("Data Type:", array_2d.dtype)  # Expected Output: Data Type: int64 (or similar, depending on system)
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
