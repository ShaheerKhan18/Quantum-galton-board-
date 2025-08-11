# Project Name
Project 1
Quantum Walks and Monte Carlo

# Team Name
Coherent Walkers

# Name and Wiser ID
Shaheer Khan - gst-GU9x0TqNmaE22J5
Mahroo Mirabdolhagh  - gst-vW0WphXNPKu0XHC

# Project Summary
A Galton board is a triangular array of pegs with bins below the last layer of pegs. When a ball is dropped onto the top peg, it bounces on the pegs with 50% probability to fall in either direction. It bounces all the way to the bins. Dropping an adequate number of balls creates a normal distribution.

We reviewed the paper which discusses the quantum analog of this Galton board. The Quantum Galton Board (QGB) is not limited to a bell curve. The quantum gates could be modified to obtain various distributions. We started by analyzing the level 1 and 2 of the QGB. Each peg in QGB is modelled with a Hadamard gate as it creates equal superposition in left and right possible paths. The ball is entangled with a control qubit and changes its position with control swaps. We need 2*n+2 qubits to implement an n-level quantum Galton board. The control qubit (which starts over at each level) becomes entangled with the data qubits (which still have positional information) in these CNOT gates, and we use this entanglement to monitor where the walker could be and to create either constructive or destructive interference in amplitude—simulating a quantum walk that preserves unitarity and coherence.

We wrote a Python function Game(l) that dynamically builds a QGB circuit for any number of layers l. For a QGB of l levels, the circuit requires l Hadamard gates and l reset gates (to initialize the ancilla at each level), along with a single X gate to place the “ball” in motion. Each “peg” in the board structure needs 4 gates, and since the number of pegs grows as a triangle number, this contributes a total of 2l(l + 1) gates. To measure we need l + 1 measurement gates. The total bound for this theoretical model requires n² + 5n + 2 gates.

A quantum Galton board illustrates an example where equal initial probability amplitudes yield a Gaussian distribution, with quantum interference producing a symmetric bell-shaped curve similar to the classical central limit theorem. By employing some biased rotations in the circuit, we can yield an exponential distribution where probabilistic measurements drop quickly from one side. We have demonstrated that with quantum control of interference and the manipulation of gate parameters, we can engineer output distributions with the potential to generate either symmetric or skewed patterns.

A Hadamard quantum walk is the quantum version of a classical random walk, where a “coin” qubit defines whether to move left or right. In contrast to a classical walk's Gaussian distribution, the quantum version yields a distribution with sharp peaks near the edges and much lower probabilities in the center due to quantum interference. We implemented this with a Galton-board–style quantum circuit: a coin qubit is rotated Hadamard-like at each level, followed by controlled swap gates to shift a position qubit. After a number of levels, a position register was measured and the results computed in order to derive position probabilities. This revealed the characteristic tall-edge, low-center shape of the Hadamard walk distribution.



# Project Presentation

it is main folder
