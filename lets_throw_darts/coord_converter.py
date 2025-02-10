import numpy as np


def circ_to_cart(
    radius: float | np.ndarray, angle: float | np.ndarray
) -> tuple[float | np.ndarray, float | np.ndarray]:
    """
    Convert circular coordinates to cartesian

    Parameters
    ----------
    radius: float
        radius in mm
    angle: float
        angle in radians from y-axis

    Returns
    -------
    tuple[float, float]
        (x, y) coordinates in mm
    """
    x = radius * np.sin(angle)
    y = radius * np.cos(angle)
    return x, y


def cart_to_circ(
    x: float | np.ndarray, y: float | np.ndarray
) -> tuple[float | np.ndarray, float | np.ndarray]:
    """
    Convert cartesian coordinates to circular

    Parameters
    ----------
    x: float
        x coordinate in mm
    y: float
        y coordinate in mm

    Returns
    -------
    tuple[float, float]
        (radius, angle) in [mm] and radians from y-axis
    """
    radius = np.sqrt(np.square(x) + np.square(y))
    angle = np.arctan2(x, y)
    return radius, angle % (2 * np.pi)
