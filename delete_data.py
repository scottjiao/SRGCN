import os
import sys
import shutil
path=os.path.dirname(os.path.abspath(__file__))
for models in ['srgcn','gcn']:
    modelpath=os.path.join(path,model)
    for dirname in next(os.walk(modelpath))[1]:
        if 'label' in dirname:
            shutil.retree(os.path.join(modelpath,dirname))