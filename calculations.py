import math

import matplotlib
matplotlib.use('Agg') # Fixes threading issue when creating a plot. 
import matplotlib.pyplot as plt

import os.path


# CSV FORMAT 
# z, y, x, concentration
CSV_FILE = 'concentration.timeseries.csv'

# Columns that relate to the csv file. 
Z_COLUMN = 0
Y_COLUMN = 1 
X_COLUMN = 2 
CONCENTRATION_COLUMN = 3

# Image file path 
IMAGE_DIRECTORY = 'images'

# File name for png 
IMAGE_NAME = 'output-1.png'

# Hold data in these variables so we don't recalculate each time a request is made. 
CONCENTRATION_SUM = -1
CONCENTRATION_STD = -1
CONCENTRATION_MEAN = -1
CONCENTRATION_IMAGE_PATH = ''

# Read the data from the csv file into a string. 
def __getData():

    #opening csv file containing our data.
    file = open(CSV_FILE)

    #skipping first line which contains header data.
    data = file.readlines()[1:]
    file.close() 

    return data


# calculates the mean of the concentration column in the csv file. 
def __calculateMean():
    
    data = __getData()

    sum = 0 
    dataPoints = 0 

    for row in data: 
        csvSplit = row.strip().split(',')
        sum += float(csvSplit[CONCENTRATION_COLUMN])
        dataPoints += 1
    
    return sum / dataPoints

# Calculates the sum of the concentration column of the csv file. 
def __calculateSum():

    data = __getData()

    sum = 0 
    for row in data: 
        csvSplit = row.strip().split(',')
        sum += float(csvSplit[CONCENTRATION_COLUMN])
    
    return sum

# calculates the standard devation of the concentration column in the csv file. 
def __calculateStd():

    data = __getData()

    mean = __calculateMean()

    sd = 0
    dataPoints = -1
    for row in data:
        csvSplit = row.strip().split(',')
        sd += pow(float(csvSplit[CONCENTRATION_COLUMN]) - mean, 2)
        dataPoints += 1
    
    sd = math.sqrt(sd / (dataPoints))
    return sd

# Creates image of 3-d plot of the csv Data. 
def __createImage():
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    data = __getData()

    for row in data:
        csvSplit = row.strip().split(',')

        xs = float(csvSplit[X_COLUMN])
        ys = float(csvSplit[Y_COLUMN])
        concentration = float(csvSplit[CONCENTRATION_COLUMN])

        ax.scatter(xs, ys, concentration, marker='x')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Concentration')

    imageFilePath = os.path.join(IMAGE_DIRECTORY, IMAGE_NAME)
    plt.savefig(imageFilePath)
    
    return imageFilePath

# Getters 

def getSum():
    global CONCENTRATION_SUM
    if CONCENTRATION_SUM == -1:
        CONCENTRATION_SUM = __calculateSum()
    
    return CONCENTRATION_SUM

def getMean():
    global CONCENTRATION_MEAN
    if CONCENTRATION_MEAN == -1:
        CONCENTRATION_MEAN = __calculateMean()

    return CONCENTRATION_MEAN

def getStd():
    global CONCENTRATION_STD
    if CONCENTRATION_STD == -1: 
        CONCENTRATION_STD = __calculateStd()

    return CONCENTRATION_STD

def getImagePath():
    global CONCENTRATION_IMAGE_PATH
    if not os.path.isfile(CONCENTRATION_IMAGE_PATH):
        CONCENTRATION_IMAGE_PATH = __createImage()
    
    return CONCENTRATION_IMAGE_PATH

def setUp():
    global CONCENTRATION_IMAGE_PATH
    CONCENTRATION_IMAGE_PATH = __createImage()

    global CONCENTRATION_STD
    CONCENTRATION_STD = __calculateStd()

    global CONCENTRATION_SUM
    CONCENTRATION_SUM = __calculateSum()
    
    global CONCENTRATION_MEAN
    CONCENTRATION_MEAN = __calculateMean()