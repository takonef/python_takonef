import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 4):
    y = np.loadtxt('signal0' + str(i) +'.dat')

    cumsum = np.cumsum(np.insert(y, 0, 0))
    indices = np.arange(1, len(y) + 1)
    start_indices = np.maximum(0, indices - 10)

    window_sums = cumsum[indices] - cumsum[start_indices]
    window_sizes = indices - start_indices
    filtered = window_sums / window_sizes

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(y, linewidth=1.5)
    ax1.set_title("Raw", fontsize=14)
    ax1.set_xlabel("Time")
    ax1.set_ylabel("Value")
    ax1.grid(True, linestyle='--', alpha=0.6)

    ax2.plot(filtered, linewidth=1.5)
    ax2.set_title("Filtered", fontsize=14)
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Value")
    ax2.grid(True, linestyle='--', alpha=0.6)

    plt.subplots_adjust(wspace=0.3) #
    plt.savefig('filtered' + str(i) + '.png')
    plt.show()  