from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.visualization import plot_histogram
import numpy as np


# Parameters for Hadamard coin: U(theta=pi/2, phi=0, lam=pi)
theta = np.pi / 2
phi = 0
lam = np.pi

# Backend and shots
backend = Aer.get_backend("qasm_simulator")
shots = 10000

qc = QuantumCircuit()
q = QuantumRegister(10, 'q')
c = ClassicalRegister(7, 'c')

qc.add_register(q)
qc.add_register(c)

qc.reset(q[0])
qc.x(q[5])

# Set initial symmetric coin state: 1/sqrt(2) (|0> + i|1>)
qc.h(q[0])
qc.s(q[0])

# First level: Hadamard coin flip
qc.u(theta, phi, lam, q[0])
qc.cswap(q[0], q[4], q[5])
qc.cx(q[5], q[0])
qc.cswap(q[0], q[5], q[6])

# Second level: Hadamard coin flip (no reset)
qc.u(theta, phi, lam, q[0])
qc.cswap(q[0], q[3], q[4])
qc.cx(q[4], q[0])
qc.cswap(q[0], q[4], q[5])
qc.cx(q[5], q[0])
qc.cswap(q[0], q[6], q[7])
qc.cx(q[6], q[0])
qc.cswap(q[0], q[5], q[6])

# Third level: Hadamard coin flip (no reset)
qc.u(theta, phi, lam, q[0])
qc.cswap(q[0], q[2], q[3])
qc.cx(q[3], q[0])
qc.cswap(q[0], q[3], q[4])
qc.cx(q[4], q[0])
qc.cswap(q[0], q[7], q[8])
qc.cx(q[7], q[0])
qc.cswap(q[0], q[6], q[7])
qc.cx(q[6], q[0])
qc.cswap(q[0], q[5], q[6])
qc.cx(q[5], q[0])
qc.cswap(q[0], q[4], q[5])

# Fourth level: Hadamard coin flip (no reset)
qc.u(theta, phi, lam, q[0])
qc.cswap(q[0], q[1], q[2])
qc.cx(q[2], q[0])
qc.cswap(q[0], q[2], q[3])
qc.cx(q[3], q[0])
qc.cswap(q[0], q[3], q[4])
qc.cx(q[4], q[0])
qc.cswap(q[0], q[4], q[5])
qc.cx(q[5], q[0])
qc.cswap(q[0], q[5], q[6])
qc.cx(q[6], q[0])
qc.cswap(q[0], q[6], q[7])
qc.cx(q[7], q[0])
qc.cswap(q[0], q[7], q[8])
qc.cx(q[8], q[0])
qc.cswap(q[0], q[8], q[9])

qc.measure(q[1], c[1])
qc.measure(q[3], c[2])
qc.measure(q[5], c[3])
qc.measure(q[7], c[4])
qc.measure(q[9], c[5])

aer_sim = Aer.get_backend('aer_simulator')
t_qc = transpile(qc, aer_sim)
result = aer_sim.run(t_qc, shots=shots).result()
counts = result.get_counts()

# --- Output ---
print("Measurement outcomes:", counts)
plot_histogram(counts)
