import numpy as np

def circ_to_cart(radius: float, angle: float) -> tuple[float, float]:
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


def cart_to_circ(x: float, y: float) -> tuple[float, float]:
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
    radius = np.square(x ** 2 + y ** 2)
    angle = np.arctan2(x, y)
    return radius, angle