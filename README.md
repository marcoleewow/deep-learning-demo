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
# Download Miniconda (Python 3.6) from:
https://conda.io/miniconda.html
```

```
# Install Miniconda by opening the terminal and run this shell script (Mac & Linux)
bash Miniconda3-latest-MacOSX-x86_64.sh
```

```
# git clone the repo
git clone git@github.com:marcoleewow/deep-learning-demo.git
cd deep-learning-demo
```

```
# create virtual environment using miniconda
conda env create -f environment.yml
```


```
# activate the conda env
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



