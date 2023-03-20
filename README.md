# DNN-GUI-CV-Model
 This repo contains a custom built model trainer for image classification application using Deep Neural Network
Development of Computer Vision based POC for Engine part inspection using Deep Neural Network

Configuration Process :-
1.	To run python file download and install the following libraries with specified versions using python package manager (pip)
PyQt5                        5.15.6
PyQt5-Qt5                    5.15.2
PyQt5-sip                    12.10.1
opencv-contrib-python        4.6.0.66
opencv-python                4.6.0.66
numpy                        1.22.4

2.	Connect camera to the PC/ Controller and run the file.
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")


3.	You should see the camera feed on the GUI 
4.	Type Dataset name for the object of interest
5.	For classification type particular class name (presence/absence, Ok/NC, Good/Bad etc.)
6.	Click on capture to capture the current frame. The pictures are then stored in the local directory of Dataset name.
7.	Particular classes are stored in sub directories in the Dataset directory
8.	Change the name of class to capture pictures of different class.
9.	Copy the path of the dataset directory and put it in NN_model file for training.
10. Put the path of Directory in the function call highlighted in blue

 


11.	Put number of iterations to train for and batch size or leave it default
12.	For inference put the input path to the function call highlighted in yellow 

13.	Run model.predict(img) cell for inference

14.	To convert the model into onnx format run following cells 

