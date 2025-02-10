import numpy as np

from lets_throw_darts.dartboard import Dartboard
from lets_throw_darts.coord_converter import cart_to_circ, circ_to_cart

def test_cartesian_there_and_back():
    """
    Test that random coords generated in cartesian and
    converted to circ and back are equal
    """
    N = 1000
    x, y = np.random.uniform(-Dartboard.radii[-1], Dartboard.radii[-1], size=(2, N))
    radii, angles = cart_to_circ(x, y)
    new_x, new_y = circ_to_cart(radii, angles)
    assert np.allclose(new_x, x)
    assert np.allclose(new_y, y)


def test_circular_there_and_back():
    """
    Test that random coords generated in circular coords and
    converted to cartesian and back are equal
    """
    N = 1000
    radii = np.random.uniform(0.0, Dartboard.radii[-1], N)
    angles = np.random.uniform(0.0, 2 * np.pi, N)
    x, y = circ_to_cart(radii, angles)
    new_radii, new_angles = cart_to_circ(x, y)

    assert np.allclose(new_radii, radii)
    print(sum(np.isclose(new_angles, angles)))
    assert np.allclose(new_angles, angles)

def test_known_angles():
    theta = np.deg2rad(270)
    radius = 10.0
    x, y = circ_to_cart(radius, theta)
    print(x, y)
    assert False