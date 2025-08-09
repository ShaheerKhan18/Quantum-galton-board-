
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

    for j in range(1, l):
        #reset and hadamard for each level
        qc.reset(0)
        qc.h(0)

        for i in range(j, 0, -2):
            if (k + i - 1)!= k:
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
        qc.reset(0)
        qc.h(0)
        for i in range(1, m - 2):
            if i%2 != 0:
                qc.cswap(0, i, i + 1)
                qc.cx(i + 1, 0)
                qc.cswap(0, i + 1, i + 2)
                if i + 1 != m - 2:
                    qc.cx(i + 2, 0)
 
    cbit = 0          
    for i in range(m):      
        if i%2 != 0:
            qc.measure(i, cbit)
            cbit += 1
           
    return qc

qc = Game(4)
#View the circuit as plain text (no matplotlib needed)
#print(qc.draw(output='text'))

from qiskit.visualization import plot_histogram
backend = Aer.get_backend("qasm_simulator")

t_qc = transpile(qc, backend)
result = backend.run(t_qc, shots=4024).result()
counts = result.get_counts()

# --- Output ---
print("Measurement outcomes:", counts)
plot_histogram(counts)
