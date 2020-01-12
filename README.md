# Person_reid_market1501

## Dataset

### Market-1501
Person re-identitification dataset collected in front of a supermarket from six different cameras. The dataset
contains 1501 different identities that are captured by at least two cameras.
[Sample code](https://github.com/justayak/pak/blob/master/samples/Market1501.ipynb)

```python
from pak.datasets.Market1501 import Market1501 

mot15 = Market1501('/place/to/store/the/data')
# if the library cannot find the data in the given directory it
# will download it and place it there..

X, Y = m1501.get_train()
```

### SOFTWARE REQUIREMENTS
* Anaconda/Miniconda
* python >=3.5
* numpy
* scipy
* skimage
* h5py


### INSTALLATION
```bash
pip install tensorflow==1.8
pip install Keras==2.1.3
pip install git
pip install https://github.com/jutanke/pak.git
conda install -c menpo opencv3 
pip install https://github.com/jutanke/person_reid.git
```
Installations can also be made with jupyter nootebook, make sure to use ! before the installation command 
```bash
!pip install tensorflow==1.8
```
For commands like conda install -c menpo opencv3 which require users to interact with the prompt Eg: proceed(y/n)? use 
```bash
conda install -c menpo opencv3 --yes
```
## STEPS
* Start menu search -> spyder
* Download the git repo --> https://github.com/Innoovatum32/Person_reid_market1501.git
* cd path/to/repo in console -spyder
* Put the images for person-reid into the folred - images01 
* Install the above mentioned libraries
* change the path for reading images to the your/path
Eg:
```bash
image02 = cv2.cvtColor(cv2.imread('path/to/your/img002.png'), cv2.COLOR_BGR2RGB)
```
* run the python script --> person_reid.py

## OUTPUT
* plots the given input images and prints the person re-identification score, given input could be "two images" or two lists of images to passed into the model reid(). 
* score of the re-identification model
![Score](https://github.com/Innoovatum32/Person_reid_market1501/blob/master/images01/Screenshot%20(36).png)

## About libraries

* pak:
*using pip install https://github.com/jutanke/pak.git* - 
Personal computer vision/deep learning dataset helper toolbox to make it less tedious to download and load common datasets. This software is not affiliated with any of the datasets but is instead just a thin helper box to ease interacting with the data.

* reid:
*using pip install https://github.com/jutanke/person_reid.git*-
This library was developed using Python 3.6, numpy, Keras 2.1.3. and tensorflow 1.8, The model is a Siamese Network using DenseNet as feature extractor. uses from keras.models import Sequential, Model & keras.layers import Dense, Dropout, Input, Flatten, concatenate with two hidden layers with dense network.

Market-1501 dataset

@inproceedings{zheng2015scalable,
  title={Scalable Person Re-identification: A Benchmark},
  author={Zheng, Liang and Shen, Liyue and Tian, Lu and Wang, Shengjin and Wang, Jingdong and Tian, Qi},
  booktitle={Computer Vision, IEEE International Conference on},
  year={2015}
}
