# Quantum Expressibility and Entangling Capability

Quantum expressibility and entangling capability calculation algorithm implemented by qiskit. See https://arxiv.org/abs/1905.10876

## Index

+ `/circuits`: sample VQC structures.
+ `/expressibility`: Quantum Expressibility Calculation Algorithm.

```python
def expressibility(qubits, sampler, *, bins=100, epoch=3000, layer=1, encode=False, return_detail=False):
    ...
    # in which sampler(layer=layer, qubits=qubits)
```

+ `/entanglement`: Quantum Entanglement Capability calculation algorithm.

```python
def Ent(sampler, *, epoch=3000, layer=1):
    ...
```

+ `/experiments`: Calculation Experiments