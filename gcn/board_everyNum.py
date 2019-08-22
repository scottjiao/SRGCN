from subprocess import run
import os
import numpy as np
import sys



path=os.path.dirname(os.path.abspath(__file__))
os.chdir(path)
num=10
dataset=sys.argv[2]
times=50
if len(sys.argv)>=2:
    num=int(sys.argv[1])


labelpath=os.path.join(path,'labelEveryNum'+str(num))
name='result_gcn_EveryNum{}.txt'.format(num)
try:
    os.mkdir(labelpath)
except:
    pass
os.chdir(labelpath)
print(name)


k=open(os.path.join(labelpath,name),'w')
k.close()


#****************************************************************************************
#Establish training set validation sets and test sets
np.random.seed(123)
train_file=open('train_text.txt','w')
val_file=open('val_text.txt','w')
test_file=open('test_text.txt','w')

os.chdir(path)
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

for i in range(times):

    idx_train = []
    idx_val = []
    for j in label_dict:
        train = list(np.random.choice(label_dict[j], size=num, replace=False))
        val = list(np.random.choice(list(set(label_dict[j]) - set(train)), size=num, replace=False))
        idx_train.extend([int(x) for x in train])
        idx_val.extend([int(x) for x in val])
    idx_test=list(set(list(range(NumOfItems)))-set(idx_val)-set(idx_train))
    
    
    #idx_train=list(np.random.choice(list(range(2708)),size=num,replace=False))
    #idx_val=list(np.random.choice(list(set(list(range(2708)))-set(idx_train)),size=num,replace=False))
    #idx_test=list(set(list(range(2708)))-set(idx_val)-set(idx_train))
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