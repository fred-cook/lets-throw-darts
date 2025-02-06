import numpy as np

from lets_throw_darts.dartboard import Dartboard

def get_score(radius: float, angle: float) -> int:
    """
    Calculate the score of a dart in the board

    Parameters
    ----------
    radius: float
        radius of the dart from the centre in mm
    angle: float
        angle of the dart from the y-axis in radians

    Returns
    -------
    score: int
    """
    radius_index = np.searchsorted(Dartboard.radii, radius)
    match radius_index:
        case 1:
            # bullseye
            return 50
        case 2:
            # outer
            return 25
        case 7:
            # outside scoring zone:
            return 0
        case _:
            seg_index = np.searchsorted(
                Dartboard.angles_rad + np.deg2rad(Dartboard.segment_angle/2),
                angle % (2 * np.pi)
            ) % len(Dartboard.segments)
            return Dartboard.segments[seg_index] * Dartboard.multiplier[radius_index]
        

def get_score_cartesian(x: float, y: float) -> int:
    """
    Calculate the score of a dart from cartesian coords

    Parameters
    ----------
    x: float
        x position [mm]
    y: float
        y position [mm]

    Returns
    -------
    score: int
    """
    # angle from y axis
    radius = np.sqrt(x ** 2 + y ** 2)
    angle = np.arctan2(x, y)
    return get_score(radius=radius, angle=angle)