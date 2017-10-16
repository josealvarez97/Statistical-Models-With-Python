#Exercises based on documentation of scipy.org
#https://docs.scipy.org/doc/numpy-dev/user/quickstart.html

print('''
The NumPy histogram function applied to an array returns a 
pair of vectors: the histogram of the array and the vector 
of bins. Beware: matplotlib also has a function to build 
histograms (called hist, as in Matlab) that differs from 
the one in NumPy. The main difference is that pylab.hist 
plots the histogram automatically, while numpy.histogram 
only generates the data.
''')


# Following example retrieved froM SciPy.org documentation
import numpy as np 
import matplotlib.pyplot as plt 

# Build a vector (an array) of 10000 normal deviates with variance 0.5^2 and mean 2
# Definition: A standard normal deviate (or standard normal variable)
# is a normally distributed random variable with expected value 0 and variance 1
# Clarification: A variance of 0.5^2 means a standard deviation of 0.5
# Definition: sigma refers to the standard deviation
# Definition: mu refers to the mean.
mu = 2 # the mean
sigma = 0.5 # the standard deviation
# 10000 refers to the number of elements (normal deviates), then. Probably.
# random, because we are essentially just generating frequencies between 0 and 0.9 (normal deviates)
# normal, because we, again, want a normal distribution of normal deviates.
v = np.random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
# Clarification: Now I know. bins actually refers to the number of classes
# CLARIFICATION: Normed is a boolean value. Optional.
    # if false, the result will contain the number of samples in each bin
    # if true, the result is the value of the probability density function at the bin, 
        #normalized such that the integral over the range is 1.
    #https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.histogram.html
plt.hist(v, bins=50, normed=True)
#plt.show()

# Another way: Computing the hist with numpy and then to plotting it
(n,bins) = np.histogram(v, bins=50, normed=True) # No plot using numpy
plt.plot(.5*(bins[1:]+bins[:-1]),n) #do not actually understand very well this line to be honest...
plt.show()