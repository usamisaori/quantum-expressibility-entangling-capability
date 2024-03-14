#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


from qiskit.quantum_info import state_fidelity, Statevector

def getStatevector(circuit):
    return Statevector(circuit).data


# In[5]:


import warnings
warnings.filterwarnings('ignore')


# # 1. Measure Expressibililty

# ## 1.1 Tool Functions

# In[6]:


def P_haar(N, F):
    if F == 1:
        return 0
    else:
        return (N - 1) * ((1 - F) ** (N - 2))


# In[7]:


def KL(P, Q):
    epsilon = 1e-8
    kl_divergence = 0.0
    
    for p, q in zip(P, Q):
        kl_divergence += p * np.log( (p + epsilon) / (q + epsilon) )
    
    return abs(kl_divergence)


# ## 1.2 Expressibility calculation algorithm

# In[8]:


def expressibility(qubits, sampler, *, bins=100, epoch=3000, layer=1, encode=False, return_detail=False):
    unit = 1 / bins
    limits = []
    probabilities = np.array([0] * bins)
    for i in range(1, bins + 1):
        limits.append(unit * i)

    for i in range(epoch):
        circuit_1 = sampler(layer=layer, qubits=qubits)
        circuit_2 = sampler(layer=layer, qubits=qubits)
        f = state_fidelity(
            getStatevector(circuit_1),
            getStatevector(circuit_2)
        )

        for j in range(bins):
            if f <= limits[j]:
                probabilities[j] += 1
                break

    pHaar_vqc = [ P_haar(2 ** qubits, f - (unit/2)) / bins for f in limits]
    probabilities = [ p / epoch for p in probabilities ]
    
    if return_detail:
        return pHaar_vqc, probabilities
    else:
        return KL(probabilities, pHaar_vqc)


# In[ ]:




