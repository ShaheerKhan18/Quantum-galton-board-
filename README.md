# Project Name
Project 1
Quantum Walks and Monte Carlo

# Team Name
Coherent Walkers

# Name and Wiser ID
Shaheer Khan - gst-GU9x0TqNmaE22J5
Mahroo Mirabdolhagh  - 

# Project Summary

A galton board is a triangular array of pegs with bins below the last layer of pegs. When a ball is dropped onto the top peg, it bounces on the pegs with 50% probability to fall in either direction. It bounces all the way to the bins. Dropping adequate number of balls create a normal distribution. We reviewed the paper which dicusses the quantum analog of this galton board. The Quantum Galton Board (QGB) is not limited to a bell curve. The quantum gates could be modified to obtain various distributions. 
We started by analyzing the level 1 and 2 of the QGB. Each peg in QGB is modelled with a hadamard gate as it creates equal superposition in left and right possible paths. The ball is entangled with a control qubit. and changes its position with conrrol swaps.  We need 2*n+2 qubits to implement n-level quantum Galton board. The control qubit (which starts over at each level) becomes entangled with the data qubits (which still have positional information) in these CNOT gates and we use this entanglement to Monitor where the walker could be and to Create either constructive or destructive interference in amplitude. CSWAP swaps amplitude between bins. The amplitude for the walker is spread between nearby bins. Executing these CSWAPs and then repeating at level switches simulates a quantum walk that preserves unitarity and coherence.

We wrote a Python function Game(l) that dynamically builds a QGB circuit for any number of layers l. For a QGB of l levels, the circuit requires l Hadamard gates and l reset gates (to initialize the ancilla at each level), along with a single X gate to place the “ball” in motion. Each “peg” in the board structure needs 4 gates, and since the number of pegs grows as a triangle number, this contributes a total of 2l(l + 1) gates. To measure we need l + 1 measurement gates. The total bound for this theoretical model requries n^2 + 5n + 2 gates.


#### 333 words till now. yet to add Gaussian, exponential, hadamard random walk distribution. ####


# Project Presentation


