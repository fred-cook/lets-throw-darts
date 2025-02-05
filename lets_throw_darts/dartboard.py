from dataclasses import dataclass

import numpy as np


@dataclass
class Dartboard:
    """
    Parts of a dartboard, angles and measurements as well as scores
    for each segment
    """
    segments = np.array(
        [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
    )
    segment_angle = 360.0 / len(segments)
    angles_deg = np.linspace(0.0, 360.0 - segment_angle, len(segments))
    angles_rad = np.deg2rad(angles_deg)
    radii = np.array([0.0, 6.35, 16, 99, 107, 162, 170]) #  [mm]
    radii_names = [
        "centre",
        "bull",
        "outer",
        "treble_inner",
        "treble_outer",
        "double_inner",
        "double_outer"
    ]
    multiplier = np.array([1, 1, 1, 1, 3, 1, 2])

