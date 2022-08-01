# ASP_Trucks

#
Parameters of the model:

{
 
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

}

#
Error Rate: 6.2% (62 False Positives)
#

Active leaf byte size estimate: 0.0,

Active learning nodes: 5,

Byte size estimate overhead: 1.0,

Inactive leaf byte size estimate: 0.0,

Tree depth: 3,

Tree size (leaves): 5,

Tree size (nodes): 9
#

if Attribute 0 <= 4.549969620513424:
  
  if Attribute 1 <= 5.440182925299016:
  
     Leaf = Class 0 | {0: 1483.7701231655974, 1: 126.21043791003063}
  
  if Attribute 1 > 5.440182925299016:
   
     Leaf = Class 1 | {0: 226.2298768344026, 1: 1134.7895620899694}

if Attribute 0 > 4.549969620513424:

  if Attribute 1 <= 2.7458918258475:
  
    if Attribute 0 <= 7.025831689338791:
    
      Leaf = Class 0 | {0: 346.9957515289482, 1: 80.24731419124495}
    
    if Attribute 0 > 7.025831689338791:
    
      Leaf = Class 1 | {0: 22.00424847105179, 1: 462.752685808755}
  
  if Attribute 1 > 2.7458918258475:
  
    Leaf = Class 1 | {0: 19.802776649733953, 1: 2649.539139305971}
