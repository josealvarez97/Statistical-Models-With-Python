# Exercises based on the documentation of scipy.org


import numpy as np



# 3 dimension array
myFirstNumpyArray = np.array([[[0,1,3],[2,5,6]],[[0,1,3],[2,5,6]]])
print(myFirstNumpyArray.ndim)
# 2 dimension array
myFirstNumpyArray = np.array([[0,1,3],[2,5,6],[9,9,9]]) 
print(myFirstNumpyArray.ndim)



print('EXAMPLE:')
print('[[0,1,3],[2,5,6],[9,9,9]]')
print('ndarray.ndim',end=': ')
print(myFirstNumpyArray.ndim)
print('     ...number of dimensions/axes. The rank')
print('ndarray.shape',end=': ')
print(myFirstNumpyArray.shape)
print('     ...size of the array in each dimension')
print('ndarray.size',end=': ')
print(myFirstNumpyArray.size)
print('     ...total numbers of element. Product of elements of shape.')
print('ndarray.dtyp',end=': ')
print(myFirstNumpyArray.dtype)
print('     ...object describing the type of elements in the array')
print('ndarray.itemsize',end=': ')
print(myFirstNumpyArray.itemsize)
print('     ...size in bytes of each element of the array')
print('ndarray.data',end=': ')
print(myFirstNumpyArray.data)
print('     ...position in memory that contains the element of the array. " buffer containing the actual elements of the array"')



# WAYS FOR CREATING NUMPY ARRAYS

names = np.array(['Alejandro','Javier','Jose'])

birthdates = np.array([(1,26,1993),(8,10,1995),(12,8,1997)])

#type of array can also be explicitly specified at creation time:
complexArray = np.array([[1,2],[3,4],[5,6]], dtype=complex)
#print(complexArray)


print('''
Often, the elements of an array are originally unknown, but 
its size is known. Hence, NumPy offers several functions to 
create arrays with initial placeholder content. These 
minimize the necessity of growing arrays, an expensive 
operation.
''')

print('Array Full Of Zeros: np.zeros((n,m)) <-shape is the parameter')
print(np.zeros((3,4)))
print('Array full of ones: np.ones((n,m,...))')
print(np.ones((3,4)))
print('No initialized array. Empty or random (after testing, I realized that it is not essentially random): np.empty()')
print(np.empty((3,5)))



#To create sequences of numbers

print('np.arange(15,45,5) #starting at 5 and adding up 5 until before 45')
print(np.arange(15,45,5))
print('np.linspace(15,45,3)#')
print(np.linspace(15,45,3))

# from numpy import pi
# print(np.sin([4,5]))
# x = np.linspace(0,2*pi,100)# This is useful to evaluate function at lots of points
# f = np.sin(x)
# print(f) #We just evaluated the sin of 100 angles between 0 and 2*pi
