# nlp-algorithm-design
Had to build 3.8 from source to get support for jupyterlab
https://linuxize.com/post/how-to-install-python-3-8-on-debian-10/
## Installing this Venv
This section is in a different virtual environment to the API.
First activate the VENV and install Pip packages:
```
source nlp-venv/bin/activate
pip install -r requirements.txt
```
## Run Jupyter Notebooks
```
jupyter notebook
```
## General Commands for Using Venv
Create: python3.8 -m venv my-app-venv
Activate: the environment: source my-app-venv/bin/activate
Deactivate: (my-app-venv) $ deactivate
## Installing on a new env
(in-venv) $ pip install -r requirements.txt
## Run Jupyter
$ jupyter notebook --ip=0.0.0.0 --port=8080
