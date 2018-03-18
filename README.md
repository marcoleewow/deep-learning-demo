# Deep Learning Demo

Various projects for demonstrating deep learning technology.

## Installation
```
# Install git (Mac OS)
git --version
# The above should prompt you to install git.

# for Windows please download and install git for Windows
https://git-scm.com/download/win
```

```
# Download and install Miniconda (Python 3.6):

# Mac
# Download the package
wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
bash Miniconda3-latest-MacOSX-x86_64.sh
```

Keep pressing Enter until it asks you to answer (yes/no), answer yes.
```
# once you finished installing, remove the shell script
rm Miniconda3-latest-MacOSX-x86_64.sh

# Windows go to https://conda.io/miniconda.html and download Python 3.6 installer
```


Close this terminal and reopen again for conda to work!

```
# git clone the repo
git clone https://github.com/marcoleewow/deep-learning-demo.git
```
```
# change directory
cd deep-learning-demo
```

```
# create virtual environment using miniconda
conda env create -f environment.yml
```


```
# activate the conda environment
Windows: activate myenv
macOS and Linux: source activate myenv
```


## Try out the demo!

For face recognition:

`python face-recognition-demo/facerec_from_webcam_faster.py`

For blurring face:

`python face-recognition-demo/blur_faces_on_webcam.py`

For multi style transfer (please remember to download the model first), 
note that this demo is quite slow on CPU:
```
# download the model
bash style-transfer-demo/models/download_model.sh
# run the script
python style-transfer-demo/camera_demo.py

```
For chatbot:

`python chatbot-demo/chatter_bot.py`


## Finish running demo
```
# deactivate your virtualenv
source deactivate
```



