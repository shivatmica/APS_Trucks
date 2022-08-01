# ASP_Trucks

This is a test implementation for HoeffdingTree classifier implementation from scikit-multiflow.

HoeffdingTree is also known as Very Fast Decision Tree (VFDT) is an incremental, anytime decision tree induction algorithm which is capable of learning from massive data streams.

This code tests the accuracy, error rate of VFDT on ASP dataset available at the following link:
https://www.kaggle.com/datasets/uciml/aps-failure-at-scania-trucks-data-set/code?select=aps_failure_test_set.csv


#
Parameters of the model:

 'binary_split': False,
 
 'grace_period': 200,
 
 'leaf_prediction': 'nb',
 
 'max_byte_size': 33554432,
 
 'memory_estimate_period': 1000000,
 
 'nb_threshold': 0,
 
 'no_preprune': False,
 
 'nominal_attributes': None,
 
 'remove_poor_atts': False,
 
 'split_confidence': 1e-07,
 
 'split_criterion': 'info_gain',
 
 'stop_mem_management': False,
 
 'tie_threshold': 0.05

#
Error Rate: $3.8%$
#

Active leaf byte size estimate: 0.0,

Active learning nodes: 5,

Byte size estimate overhead: 1.0,

Inactive leaf byte size estimate: 0.0,

Tree depth: 3,

Tree size (leaves): 5,

Tree size (nodes): 9
#
![image](https://user-images.githubusercontent.com/62459136/182060045-37947b0e-46f5-4a54-9f82-ada5d7f6e72c.png)
