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




######### This is for asymmetric

import numpy as np
from qiskit import QuantumCircuit
#l number of levels
def Game(l):
    #m number of qubit needed
    m = 0
    for i in range(1, l + 1):
        if i == 1:
            m = 4
        else:
            m += 2
    #building the circuit
    qc = QuantumCircuit(m, m//2)
    #Put the ball
    k = l + 1
    qc.x(k)

    # Set parameters for U gate equivalent to Hadamard with phase for symmetry
    theta = np.pi / 2
    phi = 0
    lam = np.pi

    # Initial symmetric state for coin qubit
    qc.h(0)
    qc.s(0)  # Adds i phase to |1> for symmetry

    for j in range(1, l):
        # No reset, apply U instead of H for coherent Hadamard coin at each level
        qc.u(theta, phi, lam, 0)

        for i in range(j, 0, -2):
            if (k + i - 1) != k:
                qc.cswap(0, k - i, k - i + 1)
                qc.cx(k - i + 1, 0)
                qc.cswap(0, k - i + 1, k - i + 2)
                qc.cx(k - i + 2, 0)
                qc.cswap(0, k + i, k + i - 1)
                qc.cx(k + i - 1, 0)
                qc.cswap(0, k + i - 1, k + i - 2)
                if k + i - 1 != k + 1:
                    qc.cx(k + i - 2, 0)
            elif (k + i - 1) == k:
                qc.cswap(0, k, k + 1)
                qc.cx(k, 0)
                qc.cswap(0, k, k - 1)
    if l > 2:
        # No reset, apply U for last level
        qc.u(theta, phi, lam, 0)
        for i in range(1, m - 2):
            if i % 2 != 0:
                qc.cswap(0, i, i + 1)
                qc.cx(i + 1, 0)
                qc.cswap(0, i + 1, i + 2)
                if i + 1 != m - 2:
                    qc.cx(i + 2, 0)
 
    cbit = 0          
    for i in range(m):      
        if i % 2 != 0:
            qc.measure(i, cbit)
            cbit += 1
           
    return qc

qc = Game(6)
#View the circuit as plain text (no matplotlib needed)
#print(qc.draw(output='text'))

from qiskit.visualization import plot_histogram
backend = Aer.get_backend("qasm_simulator")

t_qc = transpile(qc, backend)
result = backend.run(t_qc, shots=40240).result()
counts = result.get_counts()

# --- Output ---
print("Measurement outcomes:", counts)
plot_histogram(counts)

