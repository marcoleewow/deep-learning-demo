# Deep Learning Demo

Various projects for demonstrating deep learning technology.

## Installation

### Install git
```
# for Windows, please go to the link below to download and install git for Windows
https://git-scm.com/download/win
```
```
# For Mac, install git:
git --version
# The above should prompt you to install git.
```
### Install cmake for openCV

https://cmake.org/download/

For Windows, download the cmake-3.10.3-win64-x64.msi installer and execute the file.

For Mac, click on cmake-3.10.3-Darwin-x86_64.dmg and install like a normal Mac app.


### Install Miniconda (Python 3.6)
```
# For Windows go to https://conda.io/miniconda.html, download and install Python 3.6 installer

# For Mac, download the package
wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

# execute the shell script
bash Miniconda3-latest-MacOSX-x86_64.sh
```

Keep pressing Enter until it asks you to answer (yes/no), answer yes.
```
# once you finished installing, remove the downloaded shell script as its not needed anymore.
rm Miniconda3-latest-MacOSX-x86_64.sh

```


Remember to close the current terminal and reopen again for conda to work!

### Git clone the demo repository
```
# git clone the repo and move into the directory

git clone https://github.com/marcoleewow/deep-learning-demo.git && cd deep-learning-demo

```

### Create virtual environment using Miniconda

```
conda env create -f environment.yml
```

### Activate the conda environment

```
# For Windows: 
activate myenv
```
```
# macOS and Linux:
source activate myenv
```

You have now successfully set up everything!

## Try out the demo!

For face recognition:

`python face-recognition/facerec_from_webcam_faster.py`

For blurring face:

`python face-recognition/blur_faces_on_webcam.py`

For multi style transfer (please remember to download the model first), 
note that this demo is quite slow on CPU:
```
# download the model
bash style-transfer/models/download_model.sh
# run the script
python style-transfer/camera_demo.py
```
For chatbot:

`python chatbot/chatter_bot.py`


## Finish running demo
```
# deactivate your virtualenv
source deactivate
```



