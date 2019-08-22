# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 19:41:48 2018

@author: admin
"""
import os 
path=os.path.dirname(os.path.abspath(__file__))
os.chdir(path)
from subprocess import run

os.environ['CUDA_VISIBLE_DEVICES']='0'
#dataset='citeseer'
#dataset='pubmed'
dataset='cora'
for model in ['srgcn','gcn']:
    modelpath=os.path.join(path,model)
    #for i in [10,20,30,40,50]:
        #filename=os.path.join(modelpath,'board.py')
        #run('python {} {} {}'.format(filename,i,dataset),shell=True)
    for i in [1,3,5,7,10]:
        filename=os.path.join(modelpath,'board_everyNum.py')
        run('python {} {} {}'.format(filename,i,dataset),shell=True)











