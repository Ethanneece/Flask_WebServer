from flask import Flask
from flask import send_file

import math

import matplotlib
matplotlib.use('Agg') # Fixes threading issue when creating a plot. 
import matplotlib.pyplot as plt

import os.path

app = Flask(__name__)

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

# Read the data from the csv file into a string. 
def getData():

    #opening csv file containing our data.
    file = open(CSV_FILE)

    #skipping first line which contains header data.
    data = file.readlines()[1:]
    file.close() 

    return data

# calculates the mean of the concentration column in the csv file. 
def calculateMean():
    
    data = getData()

    sum = 0 
    dataPoints = 0 

    for row in data: 
        csvSplit = row.strip().split(',')
        sum += float(csvSplit[CONCENTRATION_COLUMN])
        dataPoints += 1
    
    return sum / dataPoints

# Calculates the sum of the concentration column of the csv file. 
def calculateSum():

    data = getData()

    sum = 0 

    for row in data: 
        csvSplit = row.strip().split(',')
        sum += float(csvSplit[CONCENTRATION_COLUMN])
    
    return sum

# calculates the standard devation of the concentration column in the csv file. 
def calculateStd():

    data = getData()

    mean = calculateMean()

    sd = 0
    dataPoints = -1
    for row in data:
        csvSplit = row.strip().split(',')
        sd += pow(float(csvSplit[CONCENTRATION_COLUMN]) - mean, 2)
        dataPoints += 1
    
    sd = math.sqrt(sd / (dataPoints))
    return sd

# Creates image of 3-d plot of the csv Data. 
def createImage():
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    data = getData()

    for row in data:
        csvSplit = row.strip().split(',')

        xs = float(csvSplit[X_COLUMN])
        ys = float(csvSplit[Y_COLUMN])
        concentration = float(csvSplit[CONCENTRATION_COLUMN])

        ax.scatter(xs, ys, concentration, marker='x')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Concentration')

    imageFilePath = os.path.join(IMAGE_DIRECTORY, 'output-1.png')
    plt.savefig(imageFilePath)
    
    return send_file(imageFilePath, '3DGraph_Concentration.png')

# Routes: 

@app.route('/get-mean')
def getMean():

    return str(calculateMean())

@app.route('/get-std-deviation')
def getStd():

    return str(calculateStd())

@app.route('/get-sum')
def getSum():

    return str(calculateSum())

@app.route('/get-image')
def getImage():

    return createImage()

if __name__ == '__main__':
    app.run()