import math

import matplotlib
matplotlib.use('Agg') # Fixes threading issue when creating a plot. 
import matplotlib.pyplot as plt

import numpy

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
isSetUp = False
concentrationSum = -1
concentrationSTD = -1
concentrationMean = -1
concentrationImagePath = ''

# Read the data from the csv file into a string. 
def __getData():

    return numpy.loadtxt(CSV_FILE, skiprows=1, delimiter=',')


# calculates the mean of the concentration column in the csv file. 
def __calculateMean(data):
    
    return numpy.mean(data, axis=0)[CONCENTRATION_COLUMN]

# Calculates the sum of the concentration column of the csv file. 
def __calculateSum(data):
    
    return numpy.sum(data, axis=0)[CONCENTRATION_COLUMN]

# calculates the standard devation of the concentration column in the csv file. 
def __calculateStd(data):

    # Calculating based on sample standard deviation. 
    return numpy.std(data, axis=0, ddof=1)[CONCENTRATION_COLUMN]

# Creates image of 3-d plot of the csv Data. 
def __createImage(data):
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for row in data:

        xs = row[X_COLUMN]
        ys = row[Y_COLUMN]
        concentration = row[CONCENTRATION_COLUMN]

        ax.scatter(xs, ys, concentration, marker='x')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Concentration')

    # Checking if directory exist. 
    if not os.path.isdir(IMAGE_DIRECTORY):
        os.mkdir(IMAGE_DIRECTORY)

    imageFilePath = os.path.join(IMAGE_DIRECTORY, IMAGE_NAME)
    plt.savefig(imageFilePath)
    
    return imageFilePath

# Getters 

def getSum():
    global concentrationSum
    global isSetUp
    
    if isSetUp:
        return concentrationSum
    
    return "Calculations we're not set up."

def getMean():
    global concentrationMean
    global isSetUp
    
    if isSetUp:
        return concentrationMean
    
    return "Calculations we're not set up."

def getStd():
    global concentrationSTD
    global isSetUp
    
    if isSetUp:
        return concentrationSTD
    
    return "Calculations we're not set up."

def getImagePath():
    global concentrationImagePath
    global isSetUp
    
    if isSetUp:
        return concentrationImagePath
    
    return "Calculations we're not set up."
    
    

def setUp():

    data = __getData()
    global concentrationImagePath
    concentrationImagePath = __createImage(data)

    global concentrationSTD
    concentrationSTD = __calculateStd(data)

    global concentrationSum
    concentrationSum = __calculateSum(data)
    
    global concentrationMean
    concentrationMean = __calculateMean(data)

    global isSetUp
    isSetUp = True