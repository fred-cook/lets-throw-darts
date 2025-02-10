from dataclasses import dataclass

from lets_throw_darts.dartboard import Dartboard

@dataclass
class CircularCoord:
    radius: float
    angle: float

single_radius = (Dartboard.radii[-2] + Dartboard.radii[-3]) / 2
double_radius = (Dartboard.radii[-1] + Dartboard.radii[-2]) / 2
treble_radius = (Dartboard.radii[-3] + Dartboard.radii[-4]) / 2

TARGETS = {
    f"{char}{i}": CircularCoord(radius=radius, angle=angle)
    for char, radius in zip(("", "D", "T"), (single_radius, double_radius, treble_radius))
    for i, angle in zip(Dartboard.segments, Dartboard.angles_rad)
}

TARGETS |= {"Bull": CircularCoord(0, 0), "Outer": CircularCoord(0, 0)}