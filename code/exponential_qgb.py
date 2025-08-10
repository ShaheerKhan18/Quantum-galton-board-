
##### EXPONENTIAL DISTRIBUTION #####

def Game_exponential(levels, theta_out=1*np.pi/4):
    nstates = 2*(levels+1)
    center = levels + 1
    

    qc = QuantumCircuit(nstates, nstates // 2)
    qc.x(center)


    # All Levels
    for l in range(1, levels+1):
        qc.reset(0)
        qc.rx(theta_out, 0)
        start = center - l

        for i in range(0, l):
            qc.cswap(0, start + (2*i), start + (2*i) + 1)
            qc.cx(start + (2*i) + 1, 0)
            qc.cswap(0, start + (2*i) + 1, start + (2*i) + 2)

    return qc





###############################################################################
###############################################################################
############################## the plotting stuff #############################
###############################################################################
###############################################################################

print("Building Backend")
backend = AerSimulator()
measure_list = list(range(1, _NSTATES, 2))
print("Adding Measure")
qc.measure(measure_list, list(range(_LEVELS+1)))
print("Transpiling")
qc_compiled = transpile(qc, backend)

# Build the output map
out_map = {}
for i in range(0, _LEVELS + 1):
    s = ["0"]*(_LEVELS + 1)
    s[_LEVELS - i] = "1"
    s = "".join(s)

    out_map[s] = i

num_trials = 1000
results_total = []
for trial in range(num_trials):
    trial_out = 0
    result = backend.run(qc_compiled, shots=1).result()
    counts = result.get_counts()
    bits = list(counts.keys())[0][::-1]

    print(f"trial: {trial}, result: {bits}", end="\r", flush=True)

    if bits in out_map:
        trial_out = out_map[bits]
        results_total.append(trial_out)
    else:
        #print(f"OUTPUT INVALID: {bits}")
        continue
print()

x = np.linspace(0, 32, 300)
gauss = norm.pdf(x, loc=16, scale=np.sqrt(5))

plt.figure(figsize=(10, 6))
plt.hist(results_total, bins=range(_LEVELS+2), density=True, alpha=0.75, edgecolor='black', label='QGB Output')
plt.xlabel("Outcome")
plt.ylabel("Probability Density")
plt.title("Figure 7: Rescaled QGB Output")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()




###### QUANTITATIVE PROOF OF EXPONENTIAL DISTRIBUTION ########

# We will fit the curve
# Count the occurrences of each unique outcome
from collections import Counter
counts = Counter(results_total)
# Get the unique outcomes (x) and their corresponding counts (y)
x_data, y_data = zip(*sorted(counts.items()))
x_data = np.array(x_data)
y_data = np.array(y_data)

# Normalize the counts to get a probability density
# This is crucial for comparing to a theoretical distribution
total_shots = len(results_total)
y_prob = y_data / total_shots


# --- 2. Define and Fit the Exponential Model ---
def exponential_func(x, a, b):
    """The exponential model: y = a * e^(b*x)"""
    return a * np.exp(b * x)

print("Fitting the exponential curve to the data...")
try:
    # Use curve_fit to find the best parameters 'a' and 'b'
    # p0 provides initial guesses to help the algorithm converge
    params, covariance = curve_fit(exponential_func, x_data, y_prob, p0=(1, -0.1))
    a_fit, b_fit = params
    fit_successful = True
    print(f"Fit successful. Equation: y = {a_fit:.4f} * e^({b_fit:.4f}x)")
except RuntimeError:
    print("Curve fit failed. The data may not be exponential.")
    fit_successful = False


# --- Plotting ---
plt.figure(figsize=(10, 6))
# Plot the experimental results as a normalized histogram
plt.bar(x_data, y_prob, edgecolor='black', alpha=0.75, label='Experimental Probability')

if fit_successful:
    # Create smooth x-values for plotting the fitted curve
    x_smooth = np.linspace(min(x_data), max(x_data), 300)
    # Plot the fitted exponential curve
    plt.plot(x_smooth, exponential_func(x_smooth, a_fit, b_fit), 'r-', linewidth=2.5,
             label=f'Fitted Exponential Curve')

# Add plot titles and labels
plt.title("QGB Output vs. Fitted Exponential Distribution", fontsize=14)
plt.xlabel("Outcome Bin", fontsize=12)
plt.ylabel("Probability Density", fontsize=12)
plt.xticks(x_data)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


_LEVELS = 5
_NSTATES = 2 * (_LEVELS + 1)
#_ANGLE_OUT = 1*np.pi/4 # Gaussian np.pi / 2

qc = Game_exponential(_LEVELS)
print(qc.draw(output = 'text'))
