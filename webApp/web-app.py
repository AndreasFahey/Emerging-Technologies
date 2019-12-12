## Authore = Andreas Fahey
## Student No. = G00346830

## Web Application Using Flask

## Imports Needed
import flask as fl
import numpy as np
import base64

from cv2 import cv2
from keras.models import load_model
from PIL import Image, ImageOps

## Load Model from Jupyter
model = load_model('../newModel.h5')

app = fl.Flask(__name__)

## Variables
## This is needed to resize the image to fit MNIST Dataset
height = 28
width = 28
size = height, width

# Routing
@app.route('/')
def home():
    ## This will Return the HTML file
    return fl.render_template('myWebApp.html')


@app.route('/predict', methods=['POST'])
def convertImage():
    ## Endode
    ## This will get image from request
    encoded = fl.request.values[('imgBase64')]

    ## Decode dataURL
    decoded = base64.b64decode(encoded[22:])

    ## Save Image
    ## Ensure this works and image.png can be viewed
    with open('image.png', 'wb') as f:
        f.write(decoded)
    
    ## Used PIL import 'image'
    userImage = Image.open("image.png")

    ## Resize the Image to suit MNIST Dataset using the PIL import 'imageOps'
    newImage = ImageOps.fit(userImage, size, Image.ANTIALIAS)

    ## Save Resized Image 
    ## Ensure this works and imageResized.png can be viewed
    newImage.save("imageResized.png")

    ## cv2 Will Load the New Images
    cv2Image = cv2.imread("imageResized.png")

    ## Convert Image to grayscale
    ## Reshape and add to nparray
    grayScaleImage = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2GRAY)
    grayScaleArray = np.array(grayScaleImage, dtype=np.float32).reshape(1, 784)
    grayScaleArray /= 255

    ## Set and Get to return model prediction
    ## Setter 
    setPrediction = model.predict(grayScaleArray)
    ## Getter
    getPrediction = np.array(setPrediction[0])

    ## Need to return highest value
    ## Should be the same as the digit thats passed
    ## For this i used np.argmax()
    predictedNumber = str(np.argmax(getPrediction))
    print(predictedNumber)

    ## This will Return Predicted Digit and will be Passed to the javascript file
    return predictedNumber

## This Stopped the Keras Multithreading issue for me
app.run(threaded=False)






