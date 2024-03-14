#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import qiskit
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt


# In[2]:


from qiskit.circuit import QuantumCircuit, Parameter


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# # 1. Circuits Sampler

# In[4]:


# theta = Parameter("θ")
# phi = Parameter("φ")
# lamb = Parameter("λ")


# ## 1.1 Circuit A

# In[5]:


def sampleCircuitA(layer=1, qubits=4):
    circuit = QuantumCircuit(qubits)
    
    for i in range(layer):
        for i in range(qubits - 1):
            circuit.cx(i, i + 1)
        circuit.cx(qubits - 1, 0)
        
        for i in range(qubits - 1):
            circuit.cx(i, i + 1)
        circuit.cx(qubits - 1, 0)
        
        circuit.barrier()
        
        for i in range(qubits):
            circuit.u3(np.random.uniform(0, 2 * np.pi), np.random.uniform(0, 2 * np.pi), np.random.uniform(0, 2 * np.pi), i)

    return circuit


# In[6]:


# circuitA = sampleCircuitA(qubits=4)
# circuitA.draw(output='mpl')


# ## 1.2 Circuit B

# In[7]:


def sampleCircuitB1(layer=1, qubits=4):
    circuit = QuantumCircuit(qubits)
    
    for i in range(qubits):
        circuit.u1(np.random.uniform(0, 2 * np.pi), i)
    
    for i in range(layer):
        for j in range(qubits - 1):
            circuit.cz(j, j + 1)
        circuit.cz(qubits - 1, 0)

        circuit.barrier()
        
        for j in range(qubits):
            circuit.u1(np.random.uniform(0, 2 * np.pi), j)

    return circuit


# In[8]:


def sampleCircuitB2(layer=1, qubits=4):
    circuit = QuantumCircuit(qubits)
    
    for i in range(qubits):
        circuit.u2(np.random.uniform(0, 2 * np.pi), np.random.uniform(0, 2 * np.pi), i)
    
    for i in range(layer):
        for j in range(qubits - 1):
            circuit.cz(j, j + 1)
        circuit.cz(qubits - 1, 0)
        
        circuit.barrier()
        
        
        for j in range(qubits):
            circuit.u2(np.random.uniform(0, 2 * np.pi), np.random.uniform(0, 2 * np.pi), j)

    return circuit


# In[9]:


def sampleCircuitB3(layer=1, qubits=4):
    circuit = QuantumCircuit(qubits)
    
    for i in range(qubits):
        circuit.u3(np.random.uniform(0, 2 * np.pi), np.random.uniform(0, 2 * np.pi), np.random.uniform(0, 2 * np.pi), i)
    
    for i in range(layer):
        for j in range(qubits - 1):
            circuit.cz(j, j + 1)
        circuit.cz(qubits - 1, 0)
        
        circuit.barrier()
        
        for j in range(qubits):
            circuit.u3(np.random.uniform(0, 2 * np.pi), np.random.uniform(0, 2 * np.pi), np.random.uniform(0, 2 * np.pi), j)
        
    return circuit


# In[10]:


# circuitB1 = sampleCircuitB1(qubits=4)
# circuitB1.draw(output='mpl')


# In[11]:


# circuitB2 = sampleCircuitB2(qubits=4)
# circuitB2.draw(output='mpl')


# In[12]:


# circuitB3 = sampleCircuitB3(qubits=4)
# circuitB3.draw(output='mpl')


# ## 1.3 Circuit C

# In[13]:


def sampleCircuitC(layer=1, qubits=4):
    circuit = QuantumCircuit(qubits)
    
    for i in range(layer):
        for j in range(qubits):
            circuit.ry(np.random.uniform(0, 2 * np.pi), j)
            
        circuit.crx(np.random.uniform(0, 2 * np.pi), qubits - 1, 0)
        for j in range(qubits - 1, 0, -1):
            circuit.crx(np.random.uniform(0, 2 * np.pi), j - 1, j)
        
        circuit.barrier()
        
        for j in range(qubits):
            circuit.ry(np.random.uniform(0, 2 * np.pi), j)
            
        circuit.crx(np.random.uniform(0, 2 * np.pi), 3, 2)
        circuit.crx(np.random.uniform(0, 2 * np.pi), 0, 3)
        circuit.crx(np.random.uniform(0, 2 * np.pi), 1, 0)
        circuit.crx(np.random.uniform(0, 2 * np.pi), 2, 1)
        
    return circuit


# In[14]:


# circuitC = sampleCircuitC(qubits=4)
# circuitC.draw(output='mpl')


# ## 1.4 Circuit D

# In[15]:


def sampleCircuitD(layer=1, qubits=4):
    circuit = QuantumCircuit(qubits)
    
    for i in range(layer):
        for j in range(qubits):
            circuit.rx(np.random.uniform(0, 2 * np.pi), j)
            circuit.rz(np.random.uniform(0, 2 * np.pi), j)
            
        for j in range(qubits - 1, -1, -1):
            for k in range(qubits - 1, -1, -1):
                if j != k:
                    circuit.crx(np.random.uniform(0, 2 * np.pi), j, k)
        circuit.barrier()
            
        for j in range(qubits):
            circuit.rx(np.random.uniform(0, 2 * np.pi), j)
            circuit.rz(np.random.uniform(0, 2 * np.pi), j)
        
    return circuit


# In[16]:


# circuitD = sampleCircuitD(qubits=4)
# circuitD.draw(output='mpl')


# ## 1.5 Circuit E

# In[17]:


def sampleCircuitE(layer=1, qubits=4):
    circuit = QuantumCircuit(qubits)

    for i in range(layer):
        for j in range(qubits):
            circuit.rx(np.random.uniform(0, 2 * np.pi), j)
            circuit.rz(np.random.uniform(0, 2 * np.pi), j)
            
        for j in range(1, qubits, 2):
            circuit.crx(np.random.uniform(0, 2 * np.pi), j, j - 1)
        
        for j in range(qubits):
            circuit.rx(np.random.uniform(0, 2 * np.pi), j)
            circuit.rz(np.random.uniform(0, 2 * np.pi), j)
        
        for j in range(2, qubits, 2):
            circuit.crx(np.random.uniform(0, 2 * np.pi), j, j - 1)
        
    return circuit


# In[18]:


# circuitE = sampleCircuitE(qubits=4)
# circuitE.draw(output='mpl')


# ## 1.6 Circuit F

# In[27]:


def sampleCircuitF(layer=1, qubits=4):
    circuit = QuantumCircuit(qubits)
    
    for i in range(layer):
        for j in range(qubits):
            circuit.rx(np.random.uniform(0, 2 * np.pi), j)
            circuit.rz(np.random.uniform(0, 2 * np.pi), j)
            
        circuit.crx(np.random.uniform(0, 2 * np.pi), qubits - 1, 0)
        for j in range(qubits - 1, 0, -1):
            circuit.crx(np.random.uniform(0, 2 * np.pi), j - 1, j)

    return circuit


# In[28]:


# circuitF = sampleCircuitF(qubits=4)
# circuitF.draw(output='mpl')


# # 2. Compose Full Circuit

# ## 2.1 Encoding Circuit

# In[24]:


def sampleEncoding(qubits):
    circuit = QuantumCircuit(qubits)
    
    for i in range(qubits):
        circuit.h(i)
        circuit.ry(np.random.uniform(0, 2 * np.pi), i)
        
    return circuit


# In[25]:


# circuit = sampleEncoding(4)
# circuit.draw(output='mpl')


# ## 2.2 Compose

# In[26]:


# demo:
# circuit = sampleEncoding(5).compose(sampleCircuitB3(layer=2, qubits=5))
# circuit.draw(output='mpl')


# In[ ]:




