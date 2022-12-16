#!/usr/bin/python

from paver.easy import *
import paver.doctools
import os
import glob
import shutil
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'src')))

import iss_astronaut

sys.path.append(os.path.dirname(__file__)) 

@task
def setup():
    sh('python -m pip install -U coverage')
    sh('python -m pip install -U pytest')
    pass


@task
def test():
    sh('python -m coverage run --source src --omit src/iss_astronaut.py -m unittest discover -s test')
    sh('python -m coverage html')
    sh('python -m coverage report --show-missing')
    pass


@task
def clean():
    for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
    for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
    for pycache in glob.glob("./__pycache__"): shutil.rmtree(pycache)
    try:
        shutil.rmtree(os.getcwd() + "/cover")
    except:
        pass
    pass


@task
@needs(['setup', 'test', 'clean'])
def default():
    pass

@task
def run():
    iss_astronaut.print_iss_information()
