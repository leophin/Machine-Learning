"""
Write a Python program to create an array of (3, 4) shape,
multiply every element value by 3 and display the new array.

Expected Output:
Original array elements:
[[ 0 1 2 3]
[ 4 5 6 7]
[ 8 9 10 11]]
New array elements:
[[ 0 3 6 9]
[12 15 18 21]
[24 27 30 33]]
"""
import numpy as np

myarray= np.arange(12).reshape(3, 4)
print("Original array elements:")
print(myarray)

for a in np.nditer(myarray, op_flags=['readwrite']):
    a[...] = 3 * a
print("New array elements:")
print(myarray)
