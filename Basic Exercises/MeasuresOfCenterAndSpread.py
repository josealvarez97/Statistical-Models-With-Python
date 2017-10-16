import numpy as np 
import matplotlib.pyplot as plt 

print('''
Two data sets with the same range and standard deviation,
 but different means.
''')
data_set_1 = np.array([1,2,1,3,4,5,6,7,8,9])
data_set_2 = np.array([6,7,6,8,9,10,11,12,13,14])

print('Dataset 1: ' + str(data_set_1))
print('Mean:' + str(np.mean(data_set_1)))
print('Standard deviation: ' + str(np.std(data_set_1)))
print('Dataset 2: ' + str(data_set_2))
print('Mean:' + str(np.mean(data_set_2)))
print('Standard deviation: ' + str(np.std(data_set_2)))


#https://matplotlib.org/api/pyplot_api.html
plt.boxplot([data_set_1, data_set_2])
plt.title("Same range & same standard dev., but different means")
plt.show()


print('''
Two data sets with the same mean and range, but different 
standard deviations
''')
data_set_3 = np.array([10,20,30,40,50])
data_set_4 = np.array([10,10,30,50,50])
print('Dataset 3: ' + str(data_set_3))
print('Mean:' + str(np.mean(data_set_3)))
print('Standard deviation: ' + str(np.std(data_set_3)))
print('Dataset 4: ' + str(data_set_4))
print('Mean:' + str(np.mean(data_set_4)))
print('Standard deviation: ' + str(np.std(data_set_4)))

plt.boxplot([data_set_3, data_set_4])
plt.title("Same mean & same range, but different standard dev.")
plt.show()

print('''
Two data sets with the same mean and standard deviation, 
but different ranges. IMPOSSIBLE, standard deviations is influenced by the range.
''')
data_set_5 = np.array([10,20,30,40,50])
data_set_6 = np.array([15,15,30,45,45])
print('Dataset 5: ' + str(data_set_5))
print('Mean:' + str(np.mean(data_set_5)))
print('Standard deviation: ' + str(np.std(data_set_5)))
print('Dataset 6: ' + str(data_set_6))
print('Mean:' + str(np.mean(data_set_6)))
print('Standard deviation: ' + str(np.std(data_set_6)))

plt.boxplot([data_set_1, data_set_2])
plt.title("Not possible to have same mean and same standard dev., but different range...")
plt.show()