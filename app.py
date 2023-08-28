from flask import Flask
from flask import send_file

import calculations
import logging

import os

app = Flask(__name__)

# displays info logs when running. 
app.logger.setLevel(logging.INFO)

# File name of the image that is sent. 
OUTPUT_IMAGE_NAME = '3D-Concentration-Display.png'

# Routes: 

@app.route('/get-mean', methods=['GET'])
def getMean():
    app.logger.info('get-mean called')

    return str(calculations.getMean())

@app.route('/get-std-deviation', methods=['GET'])
def getStd():
    app.logger.info('get-std-deviation called')

    return str(calculations.getStd())

@app.route('/get-sum', methods=['GET'])
def getSum():
    app.logger.info('get-sum called')

    return str(calculations.getSum())

@app.route('/get-image', methods=['GET'])
def getImage():
    app.logger.info('get-Image called')

    return send_file(calculations.getImagePath(), OUTPUT_IMAGE_NAME)

# Main Method
if __name__ == '__main__':
    calculations.setUp()

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)