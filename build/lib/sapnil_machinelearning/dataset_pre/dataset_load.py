'''
Created on Aug 4, 2019

@author: Nasir uddin
'''

import pandas as pd
import numpy as np
import random
    
    
def load_cvs_dataset(dataset_path):
    # Set Random seed
    np.random.seed(500)
    # Add the Data using pandas
    Corpus = pd.read_csv(dataset_path, encoding='latin-1', error_bad_lines=False)

    return Corpus


# ref:https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
def splitDataset(dataset, dataset_label, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    testcopy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(testcopy))
        trainSet.append(testcopy.pop(index))
        
    labelsize = int(len(dataset_label) * splitRatio)
    labelset = []
    testlabelcopy = list(dataset_label)
    while len(labelset) < labelsize:
        index = random.randrange(len(testlabelcopy))
        labelset.append(testlabelcopy.pop(index))    
        
    return [trainSet, testcopy, labelset, testlabelcopy]
