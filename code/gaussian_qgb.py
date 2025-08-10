import numpy as np
import matplotlib.pyplot as plt
from qiskit import transpile
from qiskit_aer import AerSimulator
from scipy.stats import norm

# Use AerSimulator
backend = AerSimulator()
qc = Game(4)
qc.measure([1, 3, 5, 7, 9], list(range(5)))
qc_compiled = transpile(qc, backend)

# Map valid outputs to integer values
one_hot_map = {
    '00001': 0,
    '00010': 1,
    '00100': 2,
    '01000': 3,
    '10000': 4
}

# Parameters
num_trials = 20000
block_size = 8
sum_results = []

# Do 20000 trials, each trial is a sum of 8 runs
for _ in range(num_trials):
    trial_sum = 0
    valid = True
    for _ in range(block_size):
        result = backend.run(qc_compiled, shots=1).result()
        counts = result.get_counts()
        # Only one output since shots=1
        bits = list(counts.keys())[0][::-1]  # reverse due to little-endian
        if bits in one_hot_map:
            trial_sum += one_hot_map[bits]
        else:
            valid = False
            break  # skip this trial if one of the outputs is invalid
    if valid:
        sum_results.append(trial_sum)

# Plotting
x = np.linspace(0, 32, 300)
gauss = norm.pdf(x, loc=16, scale=np.sqrt(5))  # just for visibility

plt.figure(figsize=(10, 6))
plt.hist(sum_results, bins=range(33), density=True, alpha=0.75, edgecolor='black', label='QGB Output')
plt.plot(x, gauss, 'r--', label='Normal($\\mu$=16, $\\sigma^2$=5)')
plt.title("Figure 7: Rescaled QGB Output vs Gaussian")
plt.xlabel("Sum of 8 outcomes")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
