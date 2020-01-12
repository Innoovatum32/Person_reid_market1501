# Person_reid_market1501

## Datasets

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

## SOFTWARE REQUIREMENTS

## INSTALLATION
## STEPS
## OUTPUT


## Install
Install the library using pip:
```bash
pip install git+https://github.com/jutanke/pak.git
```

### Requirements 

* python >=3.5
* numpy
* scipy
* skimage
* h5py
* pppr (for evaluation)

#### Install [pppr](https://github.com/justayak/pppr)
```bash
pip install git+https://github.com/justayak/pppr.git
```

### spacepy
Some datasets require to read the CDF file format from NASA. Install as follows [(taken from stackoverflow)](https://stackoverflow.com/questions/37232008/how-read-common-data-formatcdf-in-python).
```bash 
wget -r -l1 -np -nd -nc http://cdaweb.gsfc.nasa.gov/pub/software/cdf/dist/latest-release/linux/ -A cdf*-dist-all.tar.gz
tar xf cdf*-dist-all.tar.gz -C ./
cd cdf*dist
apt install build-essential gfortran libncurses5-dev
make OS=linux ENV=gnu CURSES=yes FORTRAN=no UCOPTIONS=-O2 SHARED=yes -j4 all
make install #no sudo
```
Add to .bashrc:
```bash
export CDF_BASE=$HOME/Libraries/cdf/cdf36_3-dist
export CDF_INC=$CDF_BASE/include
export CDF_LIB=$CDF_BASE/lib
export CDF_BIN=$CDF_BASE/bin
export LD_LIBRARY_PATH=$CDF_BASE/lib:$LD_LIBRARY_PATH
```
Install spacepy
```bash
pip install git+https://github.com/spacepy/spacepy.git
```

### transforms3d
Some datasets require transforms3d:
```bash
pip install transforms3d
```

## [Evaluation](https://github.com/justayak/pak/tree/master/pak/evaluation)


Market-1501 dataset

@inproceedings{zheng2015scalable,
  title={Scalable Person Re-identification: A Benchmark},
  author={Zheng, Liang and Shen, Liyue and Tian, Lu and Wang, Shengjin and Wang, Jingdong and Tian, Qi},
  booktitle={Computer Vision, IEEE International Conference on},
  year={2015}
}
