"""
Given a coordinate to aim for plot the average score for
a given noise sigma
"""

import numpy as np
import matplotlib.pyplot as plt

from lets_throw_darts.dartboard import Dartboard
from lets_throw_darts.score import get_score_vectorised
from lets_throw_darts.coord_converter import cart_to_circ

NOISE = np.array([25.0, 25.0])

def average_throw_score(x: float, y: float, repeats=1000):
    random_coords = (np.random.rand(repeats, 2) * NOISE) + np.array([x, y])
    radii, angles = cart_to_circ(*random_coords.T)
    return np.mean(get_score_vectorised(radii, angles))

x_range = np.linspace(-Dartboard.radii[-1], Dartboard.radii[-1], 1000)
y_range = np.linspace(-Dartboard.radii[-1], Dartboard.radii[-1], 1000)
X, Y = np.meshgrid(x_range, y_range)

# Compute scores for each (x, y) point
Z = np.vectorize(average_throw_score)(X, Y)


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='jet', edgecolor='none')

# Draw a circle to represent the dartboard boundary (170mm radius)
#circle = plt.Circle((0, 0), 170, color="black", fill=False, linewidth=2)
#plt.gca().add_patch(circle)

plt.show()

