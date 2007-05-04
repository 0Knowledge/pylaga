#this is my attempt at a py2exe script, it worked before but now its dead...
from distutils.core import setup
import py2exe, pygame
import glob, shutil

setup(windows=["pylaga.py"],
name='Pylaga',
version='0.0.14',
description='A small Galaga clone',
author='RJ Marsan',
author_email='RJMarsan at gmail.com',
url='http://rj.selfip.com',
)

shutil.copytree('data', 'dist/data')
shutil.copytree('enemys', 'dist/enemys')
shutil.copytree('bullets', 'dist/bullets')
shutil.copytree('guns', 'dist/guns')
shutil.copytree('stages', 'dist/stages')
shutil.copyfile('freesansbold.ttf', 'dist/freesansbold.ttf')
