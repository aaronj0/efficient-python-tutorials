# efficient-python-tutorials


All of the code in the tutorial and excercises can be run by pip installing the relevant packages


### Setup WSL2/Ubuntu (Only Windows users)

Recipe:

Install Ubuntu on WSL from the Microsoft Store: https://apps.microsoft.com/detail/9pdxgncfsczv

Launch Ubuntu and run:

```
	sudo apt update
	sudo apt install python3-dev python3-venv
	sudo apt install build-essential
	python3 -m venv .venv
	source .venv/bin/activate
	pip install –upgrade pip
```

### Install Eigen:

WSL/Linux Users

`sudo apt install libeigen3-dev`

MacOS Users:

`brew install eigen`

### Install pip packages

Then(WSL/Linux/MacOS) proceed to pip install the packages in a virtual environment:

```
pip install \
    cppyy \
    numpy \
    numba \
    cython \
    jupyter \
    setuptools \
    memray \
    pandas \
    line-profiler \
    pybind11 \
    awkward \
    matplotlib
```

Part of this course is inspired by and derived from work by [ENCCS](https://enccs.se) HPDA-Python course licensed under the Creative Commons Attribution license [(CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/)