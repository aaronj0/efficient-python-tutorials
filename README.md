# efficient-python-tutorials


All of the code in the tutorial and excercises can be run by pip installing the relevant packages

Setup(Windows users: WSL2/Ubuntu) recipe:

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

Then (WSL/Linux/MacOS)

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
   pybind11
```
