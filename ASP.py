""" To run, please install skicit-multiflow, and Cython
    Commands to do this are as follows:
        - pip install Cython
        - pip install scikit-multiflow
"""

import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from skmultiflow.data import SEAGenerator
from skmultiflow.trees import HoeffdingTreeClassifier
from sklearn.model_selection import train_test_split

def neg_pos(data):
    if data > 0:
        return 1
    else: 
        return 0

trainDf = pd.read_csv('aps_failure_training_set_processed_8bit.csv')
testDf = pd.read_csv('aps_failure_test_set_processed_8bit.csv')

trainDf['class'] = trainDf['class'].apply(neg_pos) # labels changed to either 0 or 1 based on its parity 
testDf['class'] = testDf['class'].apply(neg_pos)

X = trainDf.drop('class', axis = 1)
y = trainDf['class']

X_test = testDf.drop('class', axis = 1)
y_test = testDf['class']

print(X_test)

stream = SEAGenerator(random_state=1)
ht = HoeffdingTreeClassifier()

curr_samples = 0
tp = 0
max_samples = 200
'''
ht.fit(X, y)
y_pred = ht.predict(X_test)'''

while curr_samples < max_samples and stream.has_more_samples():
    X_test, y_test = stream.next_sample()
    y_pred = ht.predict(X_test)
    if y_test[0] == y_pred[0]:
        tp += 1
    ht = ht.partial_fit(X_test, y_test)
    curr_samples += 1

print('{} samples analyzed.'.format(curr_samples))
print('Hoeffding Tree accuracy: {}'.format(tp / curr_samples))
