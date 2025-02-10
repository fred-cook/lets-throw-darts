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
                Dartboard.angles_rad + np.deg2rad(Dartboard.segment_angle / 2),
                angle % (2 * np.pi),
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
    radius = np.sqrt(x**2 + y**2)
    angle = np.arctan2(x, y)
    return get_score(radius=radius, angle=angle)


def get_score_vectorised(radii: np.ndarray, angles: np.ndarray) -> np.ndarray:
    """
    Calculate many scores at once
    """
    bulls_mask = radii < Dartboard.radii[1]
    outers_mask = (radii < Dartboard.radii[2]) ^ bulls_mask
    no_score_mask = radii > Dartboard.radii[-1]

    seg_indices = np.searchsorted(
        Dartboard.angles_rad + np.deg2rad(Dartboard.segment_angle / 2), angles
    ) % len(Dartboard.angles_rad)
    multiplier_indices = np.searchsorted(
        Dartboard.radii, radii
    )
    scores = Dartboard.segments[seg_indices] * Dartboard.multiplier[multiplier_indices]
    scores[bulls_mask] = 50
    scores[outers_mask] = 25
    scores[no_score_mask] = 0
    return scores


if __name__ == "__main__":
    from timeit import timeit

    N = 10000
    radii = np.random.uniform(0.0, Dartboard.radii[-1] + 20.0, N)
    angles = np.random.uniform(0.0, 2 * np.pi, N)

    globs = {
        "get_score": get_score,
        "get_score_vectorised": get_score_vectorised,
        "radii": radii,
        "angles": angles,
    }
    number = 100
    a = timeit("[get_score(r, theta) for r, theta in zip(radii, angles)]", globals=globs, number=number)
    b = timeit("get_score_vectorised(radii, angles)", globals=globs, number=number)

    print(f"non-vectorised: {a / number:.4f}s, {a / (number * N)} / throw")
    print(f"vectorised:     {b / number:.4f}s, {b / (number * N)} / throw")
    print(f"{a / b:.2f}x speed up")
