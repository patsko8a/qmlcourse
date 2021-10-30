.ONESHELL:
SHELL = /bin/bash

export PATH := $(HOME)/.poetry/bin:$(PATH)

install-ubuntu-latest: install-python-poetry-ubuntu install-python-dependencies
install-macos-latest: install-python-poetry-macos install-python-dependencies
install-windows-latest: 
	install-software-windows
	refreshenv
	create-condaenv-windows


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

#### WINDOWS ####

 
install-choco-windows:
	Set-ExecutionPolicy Bypass -Scope Process -Force;
	.\ChocolateyInstallNonAdmin.ps1

install-make-windows:
	choco install make curl

install-miniconda-windows:
	curl -0 https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
	cmd /C "Miniconda3-latest-Windows-x86_64.exe /S /InstallationType=JustMe /AddToPath=0 /RegisterPython=1 /D=%UserProfile%\Miniconda3"

install-software-windows: install-choco-windows install-make-windows install-miniconda-windows

create-condaenv-windows:
	cmd /C "conda create -n qmlcourse python=3.8 --yes"

install-tfq-windows:
	cmd /C "conda activate qmlcourse && python -m pip install tensorflow==2.5.1 --yes && python -m pip install -U tensorflow-quantum --yes"

install-psi4-windows:
	cmd /C "conda activate qmlcourse && conda install psi4 python=3.8 -c psi4 -c conda-forge --yes"

install-packages-windows:
	install-tfq-windows
	install-psi4-windows

install-build-packages-windows:
	cmd /C "conda activate qmlcourse && pip install -U jupyter-book"

test-psi4-windows:
	cmd /C "conda activate qmlcourse && python - m psi4 --test

build-windows:
	install-build-packages-windows
	cmd /C "conda activate qmlcourse && python -m jupyter-book build ./qmlcourseRU"



# install-psi4:
# 	bash Psi4conda-1.4rc3-py38.sh -b -u -p $(HOME)/psi4conda
# 
# install-conda-ubuntu:
# TODO
# curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh | sh ./Miniconda3-latest-Linux-x86_64.sh 
# 
# install-conda-macos:
# https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh



