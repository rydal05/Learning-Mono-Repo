L = list(range(10))
print(L, type(L[0]))

L2 = [str(c) for c in L]
print(L2, type(L2[0]))

#heterogenous lists
L3 = [True, "2", 3.0, 4]
print([type(item) for item in L3])

import numpy as np
print(np.array([1,4,5,2,3,5])) # integer compliant
print(np.array([1,4,5,2,3.14,5])) # upcast to floating
print(np.array([1,4,5,2,3,5], dtype='float32'))

print(np.array([range(i,i+3) for i in [2,4,6]])) # multidimensional array

np.array(10,dtype=int) # creating a 10 length int array initialized with 0s
print(np.full((3,5),3.14)) # a 3x5 array filled with 3.14 (3 row, 5 col)

np.arange(0,20,2) # linearly filled array, starts at 0, counts to 20, increments by 2. similar to range builtin

print(np.linspace(0,1,5)) # an array of 5 values justified from 0 and 1

np.random.random((3,3)) # creates a 3x3 array of uniformly distributed values between 0 and 1

np.zeros(10, dtype="int16")
np.zeros(10, dtype=np.int16) # both legal ways to cast an array as types