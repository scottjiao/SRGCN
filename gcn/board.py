# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 13:13:19 2018

@author: admin
"""

from subprocess import run
import os
import numpy as np
import sys



path=os.path.dirname(os.path.abspath(__file__))
os.chdir(path)
num=50

times=50
dataset=sys.argv[2]
if len(sys.argv)>=2:
    num=int(sys.argv[1])
    
labelpath=os.path.join(path,'labelSumNum'+str(num))
name='result_gcn_SumNum{}.txt'.format(num)
print(name)
try:
    os.mkdir(labelpath)
except:
    pass
os.chdir(labelpath)



k=open(os.path.join(labelpath,name),'w')
k.close()


label_file=open(os.path.join(path,'{}_labels.txt'.format(dataset)),'r')
label_dict={}
NumOfItems=0
for line in label_file:
    if line.strip('\n'):
        line=line.strip('\n').split(' ')
        NumOfItems+=1
        if line[1] not in label_dict:
            label_dict[line[1]]=[]
        else:
            label_dict[line[1]].append(line[0])
    
label_file.close()   





np.random.seed(123)
train_file=open('train_text.txt','w')
val_file=open('val_text.txt','w')
test_file=open('test_text.txt','w')

for i in range(times):
    idx_train=list(np.random.choice(list(range(NumOfItems)),size=num,replace=False))
    idx_val=list(np.random.choice(list(set(list(range(NumOfItems)))-set(idx_train)),size=num,replace=False))
    idx_test=list(set(list(range(NumOfItems)))-set(idx_val)-set(idx_train))
    train_file.write(str(idx_train)+'\n')
    val_file.write(str(idx_val)+'\n')
    test_file.write(str(idx_test)+'\n')
train_file.close()
val_file.close()
test_file.close()

os.chdir(path)
for i in range(times):
    #os.system("python train_pipeline.py {} {} {}".format(i,num,name))
    run("python train_pipeline.py {} {} {} {} {}".format(i,num,name,labelpath,dataset),shell=True)