# handwritten_recognition_tensorflow
Handwritten digits recognition with tensorflow

This repository refer to the blog [Using TensorFlow<sup>TM</sup> to create your own handwriting recognition engine](http://niektemme.com/2016/02/21/tensorflow-handwriting/) and [Tensorflow|softmax bp nn|mnist数据集](http://www.math1as.com/index.php/archives/294/#comment-55). 

## Installation & Setup

### Overview
This project uses two algorithms to train on the MNIST database. One is BP neural network(BPNN), the other is Convolution neural network(CNN). After training, the CNN training model will be saved. In another python script, the model will be restored to predict. At last, the Python GUI script achieves the handwritten digit recognition system package.

This projects consists of four scripts: 

1. *bpnn_train.py* – train on the MNIST dataset with BPNN algorithm.
2. *cnn_train.py* – train on the MNIST dataset with CNN algorithm and create the train model model.ckpt file.
3. *model.py* – achieve the images in the MNIST test set and save them in a new folder.
4. *convert.py* – convert the colour of background and digit and save the new images in a new folder.
5. *suiji.py* – randomly select 100 images from the folder above and save in a new folder.
6. *predict.py* – uses the model.ckpt file to predict the correct integers from 100 images above.
7. *predict_ui.py* – Python GUI script to display handwritten digit recognition.

### Dependencies
The following Python libraries are required.

- sys - should be installed by default
- tensorflow - [TensorFlow](https://www.tensorflow.org/)
- PIL – [Pillow](http://pillow.readthedocs.org)
- numpy – [NumPy](http://www.numpy.org/)
- pyQt – [PyQt](https://www.riverbankcomputing.com/software/pyqt)

### Installing TensorFlow
Of course TensorFlow needs to be installed. The [TensorFlow website](https://www.tensorflow.org/versions/master/get_started/index.html) has a good manual .

### Installing Python Image Library (PIL)
The Python Image Library (PIL) is no longer available. Luckily there is a good fork called Pillow. Installing is as easy as:

```sudo apt-get install python-pip```

```sudo pip install Pillow```

### Installing Numerical Python (NumPy)
NumPy is the fundamental package for scientific computing with Python. Installing is as easy as:

```sudo apt-get install python-numpy```

### Installing PyQt
PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in. Installing is as easy as:

```sudo apt-get install python-qt4```

Or look at the [PyQt4 Download](https://www.riverbankcomputing.com/software/pyqt/download) for other installation options.

## Running
Running is based on the steps:

1. train with BPNN and CNN and create the CNN train model file
2. prepare handwritten digit images 
3. predict the integers 
4. GUI to display

### 1. train with BPNN and CNN and create the CNN train model file
The easiest way is to cd to the directory where the python files are located. Then run in the terminal:

```python bpnn_train.py```

and

```python cnn_train.py```

to achieve the different training accuracy and save the CNN train model.

### 2. prepare handwritten digit images 
You have to create a PNG file that contains a handwritten number. The background has to be white and the number has to be black. Any paint program should be able to do this. Also the image has to be auto cropped so that there is no border around the number. So first run:

```tar zxvf FileName.tar.gz```

to unzip the MNIST dataset files. Then run:

```python model.py```

to resolve the images from MNIST test set. Then run:

```python convert.py```

to convert the colour of image background and digit. Then run:

```python suiji.py```

to select 100 images from the converted images randomly.


### 3. predict the integers

In the predict scripts, you need to change the correct path to the random images. Then run:

```python predict.py```

to show the 100 images and save the predicted integers in the txt file. 

### 4. GUI to display
A simple package of handwritten digit recognition system in PyQt can display directly. Run:

```python predict_ui.py```

to show a window on the screen. Click the button "input handwritten digit pictures" to choose a handwritten digit image. Then click the button "predicted number" and you can see the result in the Textbox on the window. (Path must be English.)



