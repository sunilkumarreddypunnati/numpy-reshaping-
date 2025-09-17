'''Question 1: NumPy Reshaping Practice

Task:
Given the following 1D NumPy array:

[1, 2, 3, 4, 5, 6, 7, 8]


Perform the following tasks in order:
Reshape it into a 2×4 array and print it.
Flatten the reshaped array using .flatten() and print it.
Ravel the reshaped array using .ravel() and print it.
Change the first element of the ravelled array to 100 and 
print the reshaped array again to see if it has changed.
Expected Output:

Reshaped (2x4):
[[1 2 3 4]
 [5 6 7 8]]

Flattened:
[1 2 3 4 5 6 7 8]

Ravelled:
[1 2 3 4 5 6 7 8]

Reshaped after modifying ravelled:
[[100   2   3   4]
 [  5   6   7   8]]'''

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])

#Reshaping
reshape=arr.reshape(2,4)
print("Reshaped(2x4):\n",reshape)

#Flattened
flatten=reshape.flatten()
print("Flattened:\n",flatten)

#Ravelled
ravelled=reshape.ravel()
print("Ravelled:\n",ravelled)

#modified
ravelled[0]=100
print("Reshaped after modifying ravelled:\n",reshape)


