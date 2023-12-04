import matplotlib.pyplot as plt
import numpy as np

def plot_devanagari_i():
    t = np.linspace(0, 2*np.pi, 100)

    # Parametric equations for the curves and lines forming इ
    x_top = 0.25 * np.cos(t)
    y_top = 0.25 * np.sin(t) + 0.75

    x_stem = np.array([0.0, 0.0])
    y_stem = np.array([0.0, 0.75])

    fig, ax = plt.subplots()

    # Plotting the curves and lines using parametric equations
    ax.plot(x_top, y_top, color='black')
    ax.plot(x_stem, y_stem, color='black')

    # Set axis limits and remove ticks for better visualization
    ax.set_xlim(-0.4, 0.4)
    ax.set_ylim(-0.1, 1)
    ax.axis('off')

    plt.show()

# Plotting the letter इ using parametric equations
plot_devanagari_i()
