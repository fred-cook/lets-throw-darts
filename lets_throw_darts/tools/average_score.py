"""
Given a coordinate to aim for plot the average score for
a given noise sigma
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from lets_throw_darts.dartboard import Dartboard
from lets_throw_darts.score import get_score_vectorised
from lets_throw_darts.coord_converter import cart_to_circ


def get_average_score(
    noise: np.ndarray, repeats: int, coords: np.ndarray
) -> np.ndarray:
    """
    Calculate the average score for `repeats` throws of a dart with
    gaussian `noise` added in cartesian to the supplied `coords`

    Parameters
    ----------
    noise: np.ndarray
        x and y standard deviations in mm
    repeats: int
        how many times to throw a dart at each given coordinates
    coords: np.ndarray
        columns of [x, y] positions in mm

    Returns
    -------
    average_scores: int
        the average score for each coord in the supplie coords
        for the given noise
    """
    x, y = coords.T

    # broadcast to 2D with N repeats per row
    x = x[:, None] * np.ones(repeats)
    y = y[:, None] * np.ones(repeats)

    # add noise
    x += np.random.randn(*x.shape) * noise[0]
    y += np.random.randn(*y.shape) * noise[1]

    # flatten and calcualate the scores
    average_scores = get_score_vectorised(*cart_to_circ(x.flatten(), y.flatten()))
    # put back into shape and average by row
    return average_scores.reshape(-1, repeats).mean(axis=1)


points_per_row = 250

x_range = np.linspace(-Dartboard.radii[-1], Dartboard.radii[-1], points_per_row)
y_range = np.linspace(-Dartboard.radii[-1], Dartboard.radii[-1], points_per_row)
X, Y = np.meshgrid(x_range, y_range)

X = X.flatten()
Y = Y.flatten()

# calculate points inside the dartboard
xy = np.c_[X, Y]
mask = np.linalg.norm(xy, axis=1) <= Dartboard.radii[-1]

fig, axs = plt.subplots(ncols=3, figsize=(15, 5))

noises = np.array(
    [
        [5.0, 5.0],
        [10.0, 10.0],
        [10.0, 25.0],
    ]
)

averages = [get_average_score(noise, 1000, xy[mask]) for noise in noises]

vmin, vmax = 0.0, max([np.max(avg) for avg in averages])
cmap = plt.cm.rainbow
norm = mcolors.Normalize(vmin=vmin, vmax=vmax)

for ax, avg, noise in zip(axs, averages, noises):
    z = np.zeros(len(xy))
    z[mask] = avg
    ax.set_title(f"Noise x: {noise[0]:.1f}mm, y: {noise[1]:.1f}mm")
    _ = ax.imshow(
        z.reshape(points_per_row, points_per_row), origin="lower", cmap=cmap, norm=norm
    )
    ax.set_axis_off()

cbar = fig.colorbar(_, ax=axs, orientation='vertical', fraction=0.02, pad=0.05)
#cbar.set_label("Average score")

plt.show()
