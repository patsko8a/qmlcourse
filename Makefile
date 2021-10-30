.ONESHELL:
SHELL = /bin/bash

export PATH := $(HOME)/.poetry/bin:$(PATH)

install-ubuntu-latest: install-python-poetry-ubuntu install-python-dependencies
install-macos-latest: install-python-poetry-macos install-python-dependencies

install-python-poetry-ubuntu:
	sudo apt update
	sudo apt install curl wget python3.8 -y
	sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
	sudo apt install python3-distutils -y
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3

#	curl "http://vergil.chemistry.gatech.edu/psicode-download/Psi4conda-1.4rc3-py38-Linux-x86_64.sh" -o Psi4conda-1.4rc3-py38.sh --keepalive-time 2

install-python-poetry-macos:
	brew update
	brew install zlib pyenv poetry

	pyenv install 3.8.10
	pyenv local 3.8.10

#	curl "http://vergil.chemistry.gatech.edu/psicode-download/Psi4conda-1.4rc3-py38-MacOSX-x86_64.sh" -o Psi4conda-1.4rc3-py38.sh --keepalive-time 2

install-python-dependencies:
#	poetry env use python3.8
	poetry env list
	poetry install

build-linux-macos:
#	cd $(HOME)/psi4conda/etc/profile.d/ && source conda.sh && conda activate && cd - && poetry run psi4 --test
	poetry run jupyter-book build ./qmlcourseRU

install-windows:
	conda create -n qmlcourse python=3.8 --yes
	conda activate qmlcourse
	python -m pip install --upgrade pip
	python -m pip install poetry
	python -m pip install tensorflow==2.5.1
	python -m pip install -U tensorflow-quantum
	conda install psi4 python=3.8 -c psi4 -c conda-forge
	python -m poetry install
	
build-windows:
        python - m poetry run psi4 --test
	python -m poetry run jupyter-book build ./qmlcourseRU

# install-psi4:
# 	bash Psi4conda-1.4rc3-py38.sh -b -u -p $(HOME)/psi4conda
