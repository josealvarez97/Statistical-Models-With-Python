import csv
import matplotlib.pyplot as plt
import numpy as np

weights = []
heights = []

# example.csv contains: name,weight,height
with open('example.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        weights.append(row[1])
        heights.append(row[2])



#https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html
plt.scatter(weights,heights,label="Luck")
#plt.show()

# https://matplotlib.org/devdocs/gallery/lines_bars_and_markers/scatter_symbol.html#sphx-glr-gallery-lines-bars-and-markers-scatter-symbol-py
plt.xlabel("Weights")
plt.ylabel("Heights")
plt.legend(loc=1)#Location of legend
plt.show()

# With a numpy array
WeightsNP = np.array(weights)
HeightsNP = np.array(heights)

# Nothing changes
plt.scatter(WeightsNP,HeightsNP)
plt.show()