'''Question 5: Flatten vs Ravel Changes

Task:
Given the array:

[[7, 8, 9],
 [10, 11, 12]]

Flatten and Ravel it.

Change the first element of the flattened array to 0.

Print the original array after modification.

Change the first element of the ravelled array to 99 
and print the original array again.

Expected Output:

Original array after flatten modification:
[[7 8 9]
 [10 11 12]]

Original array after ravel modification:
[[99  8  9]
 [10 11 12]]'''

import numpy as np
arr=np.array([[7,8,9],[10,11,12]])
f=arr.flatten()
f[0]=0
print("Original array after flatten modification:\n",arr)
r=arr.ravel()
r[0]=99
print("Original array after ravel modification:\n",arr)