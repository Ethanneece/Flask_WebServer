from flask import Flask
from flask import send_file

import calculations

app = Flask(__name__)

# File name of the image that is sent. 
OUTPUT_IMAGE_NAME = '3D-Concentration-Display.png'

# Routes: 

@app.route('/get-mean', methods=['GET'])
def getMean():

    return str(calculations.getMean())

@app.route('/get-std-deviation', methods=['GET'])
def getStd():

    return str(calculations.getStd())

@app.route('/get-sum', methods=['GET'])
def getSum():

    return str(calculations.getSum())

@app.route('/get-image', methods=['GET'])
def getImage():

    return send_file(calculations.getImagePath(), OUTPUT_IMAGE_NAME)

# Main Method
if __name__ == '__main__':
    calculations.setUp()
    app.run()