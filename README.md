This is The Repository for my Emerging Technologies Assignments for Final Year Semester 1 in 2019.

Project Overview

Model:

In this project we were tasked to create, document and train a model that imports and recognises hand-written digits using the MNIST dataset. For this i used Jupyter Lab and created a .ipynb file to start training my model. Instead of using the images provided i imported the dataset using keras. I ran a test example on the dataset with a range of 50 digits. I Saved and Plotted the Metrics to a graph to show the Accuracy and loss of my model i had trained. I was training this model for a web application, a mnist dataset digit predictor. So i saved my model as newModel.h5. I called this newModel as i already trained a model but had to change my model a bit to suit the web application as it was giving me tensorflow errors. Before diving into my web app i wanted to load the model in jupyter lab and do a prediction test. Which was successfull.

Application:

For the project we were to also create a web application to predict hand-written digits from the mnist dataset. This will allow the user to draw a digit using the mouse or touch pad. For the web application i used the flask python package. I created a python file to load the model created in jupyter along with an html file, javascript file and css file for design. I adapted the html from https://www.html5canvastutorials.com/labs/html5-canvas-paint-application/. I also called the Jquery script from this online source for my script https://code.jquery.com/jquery-3.4.1.js. For the web application you need to run the python file which i will show below and copy and paste address given into google chrome. Then the user can draw a digit in the black box area for prediction, click predict to return the prediction. You may also clear the canvas and start again. I also implemented an image and imageResized into my code so when the user predicts an image on the web app it will be store as a png. I made an image resized simply to match the size of the mnist dataset digits i did in my jupyter notebook.

How To Run:

First of all clone the repo =

git clone https://github.com/AndreasFahey/Emerging-Technologies.git

To Open Model (If Needed) = 

Make sure your in repository folder of this repo and type into Cmder:
jupyter lab

Web Application =

If you would like to view code type:
cd webApp
code .

If you would like to run web application type:
cd webApp
python web-app.py

If you would like to show web application in browser:
In this case copy and paste address provided in Cmder from running python web-app.py
http://127.0.0.1:5000/

References & Research for Project

Keras References & Research:

- https://github.com/ianmcloughlin/jupyter-teaching-notebooks/blob/master/keras-neurons.ipynb
- https://keras.io/
- https://jovianlin.io/keras-models-sequential-vs-functional/
- https://towardsdatascience.com/tensorflow-is-in-a-relationship-with-keras-introducing-tf-2-0-dcf1228f73ae

MNIST References & Research:

- https://nbviewer.jupyter.org/github/ianmcloughlin/jupyter-teaching-notebooks/blob/master/mnist.ipynb
- http://yann.lecun.com/exdb/mnist/
- https://docs.python.org/3/library/gzip.html#gzip.GzipFile

Neural Network References & Research:

- https://nextjournal.com/gkoehler/digit-recognition-with-keras
- https://skymind.ai/wiki/neural-network

Pandas References & Research:

- https://pandas.pydata.org/
- http://pandas.pydata.org/pandas-docs/stable/10min.html
- https://www.youtube.com/watch?v=dcqPhpY7tWk

Flask References & Research:

- https://palletsprojects.com/p/flask/
- https://github.com/ianmcloughlin/random-web-app

HTML & CSS References & Research:
https://www.html5canvastutorials.com/labs/html5-canvas-paint-application/

JQuery:
https://code.jquery.com/jquery-3.4.1.js.
