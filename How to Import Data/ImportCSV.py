# Reference https://pythonspot.com/en/reading-csv-files-in-python/


import csv

# DATA
# Jack,72,180
# Joe,55,111
# John,74,220
# Jun,68,150
# Jared,70,250
# Jamal,55,145
# Jakob,66,155

# Opening, reading, and printing the rows of a CSV file
with open('example.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        print(row)

# Since every row is returned as an array,
# if we want to print a specific cell we would:
print(row[0])



# A better example would be

names = []
weights = []
heights = []

with open('example.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        names.append(row[0])
        weights.append(row[1])
        heights.append(row[2])

print(names)
print(weights)
print(heights)


# for using a different delimeter, just:
# csvReader csv.reader(delimeter=';')


# In the case of many wanting to read data from multiple files
# Making our own function might be better

def readFile(filename):
    names = []
    weights = []
    heights = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            names.append(row[0])
            weights.append(row[1])
            heights.append(row[2])

        return names, weights, heights


names,weights,heights = readFile('example.csv')

print(names)
print(weights)
print(heights)