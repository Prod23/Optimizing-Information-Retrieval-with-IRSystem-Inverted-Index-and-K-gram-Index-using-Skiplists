import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt


def plot_beta_distribution(a, b, str):
    """
        Plots the beta distribution for given parameters a and b:
        Args: (int)a -> Parameter a, 
              (int)b -> Paramter b, 
              (string)str -> Title of the distribution

        Returns: (void) Prints a curve depicting beta distribution

    """
    x = np.linspace(0, 1, 200)
    y = beta.pdf(x, a, b)
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("y-probability")
    plt.title(str)
    plt.show()
