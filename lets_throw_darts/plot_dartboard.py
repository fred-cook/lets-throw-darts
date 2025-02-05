import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import numpy as np

from lets_throw_darts.dartboard import Dartboard


colours = [["black", "white"], ["red", "green"]]

fig, ax = plt.subplots(figsize=(8, 8))


for i, (r_1, r_2) in enumerate(zip(Dartboard.radii[:-1], Dartboard.radii[1:])):
    if i < 2:
        # inner/outer bull
        ax.add_patch(
            Wedge(
                (0, 0),
                r_2,
                0,
                360,
                edgecolor="k",
                facecolor=colours[1][i],
                width=r_2 - r_1,
            )
        )
    else:
        for j, angle in enumerate(Dartboard.angles_deg - 90):
            wedge = Wedge(
                (0, 0),
                r_2,
                angle - Dartboard.segment_angle / 2,
                angle + Dartboard.segment_angle / 2,
                edgecolor="k",
                facecolor=colours[i % 2][j % 2],
                width=r_2 - r_1,
            )
            ax.add_patch(wedge)

ax.set_xlim(-1.1 * Dartboard.radii[-1], 1.1 * Dartboard.radii[-1])
ax.set_ylim(-1.1 * Dartboard.radii[-1], 1.1 * Dartboard.radii[-1])

for angle, number in zip(Dartboard.angles_rad, Dartboard.segments):
    x = 1.05 * Dartboard.radii[-1] * np.sin(angle)
    y = 1.05 * Dartboard.radii[-1] * np.cos(angle)
    ax.text(
        x,
        y,
        str(number),
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="center",
        color="black",
    )

plt.show()
