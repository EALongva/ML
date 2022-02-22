# test file to prepare git repository using the github CLI

import numpy as np

import azureml.core as azu
#from azureml.core import 

T = 4; E = 3; ST = 2

testArray = np.zeros((T,E,ST))
temp = 0

for t in range(T):
    
    for e in range(E):

        for st in range(ST):

            temp += 1

            testArray[t,e,st] = temp

print(testArray[-1,-1,-1])
print(T*E*ST)