#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


from qiskit.quantum_info import partial_trace
from qiskit.quantum_info import DensityMatrix

def getDensityMatrix(circuit):
    return DensityMatrix(circuit).data


# In[5]:


import warnings
warnings.filterwarnings('ignore')


# # 1. Measure Entanglement

# ## 1.1 Tool functions

# In[3]:


def Q(circuit):
    matrix = getDensityMatrix(circuit)
    n = len(circuit.qubits)
    
    trs = []
    indexes = list(range(n))
    for i in range(n):
        sub_indexes = indexes.copy()
        sub_indexes.remove(i)
        
        rou = partial_trace(matrix, sub_indexes)
        tr = np.abs(np.trace(rou.data @ rou.data))
        trs.append(tr)
        
    tr = sum(trs)
    return 2 * (1 - tr / n)


# ## 1.2 Measure algorithm

# In[4]:


def Ent(sampler, *, epoch=3000, layer=1):
    ent = 0
    for i in range(epoch):
        ent += Q(sampler(layer=layer))
    
    return ent / epoch


# In[ ]:




