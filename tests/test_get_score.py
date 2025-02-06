import numpy as np

import pytest

from lets_throw_darts.score import get_score, get_score_cartesian
from lets_throw_darts.dartboard import Dartboard

N = 10

@pytest.mark.parametrize("radius,angle",
                         zip(np.random.uniform(Dartboard.radii[0],
                              Dartboard.radii[1],
                              N), np.random.uniform(0.0, 2*np.pi, N)))
def test_bullseye(radius: float, angle: float):
    """
    check that a few angles around the bullseye get 50
    """
    assert get_score(radius, angle) == 50

@pytest.mark.parametrize("radius,angle",
                         zip(np.random.uniform(Dartboard.radii[1],
                              Dartboard.radii[2],
                              N), np.random.uniform(0.0, 2*np.pi, N)))
def test_outer(radius: float, angle: float):
    """
    check that a few angles in the outer get 25
    """
    assert get_score(radius, angle) == 25



@pytest.mark.parametrize("radius,angle",
                         zip(np.random.uniform(Dartboard.radii[3],
                              Dartboard.radii[4],
                              N), np.random.uniform(0.0, 2*np.pi, N)))
def test_treble(radius: float, angle: float):
    """
    check that trebles are worth 3x normal
    """
    assert get_score(radius=radius, angle=angle) == 3 * get_score(radius=70.0, angle=angle)


@pytest.mark.parametrize("radius,angle",
                         zip(np.random.uniform(Dartboard.radii[-2],
                              Dartboard.radii[-1],
                              N), np.random.uniform(0.0, 2*np.pi, N)))
def test_double(radius: float, angle: float):
    """
    check that trebles are worth 3x normal
    """
    assert get_score(radius=radius, angle=angle) == 2 * get_score(radius=70.0, angle=angle)


@pytest.mark.parametrize("angle,expected",
                         [[0.0, 20],
                          [np.pi, 3],
                          [np.deg2rad(-18), 5],
                          [np.deg2rad(22), 1]])
def test_segment(angle: float, expected: int):
    """
    check that trebles are worth 3x normal
    """
    assert get_score(radius=70.0, angle=angle) == expected


@pytest.mark.parametrize("x,y,expected", [
    [0.0, 70.0, 20],
    [0.0, -70.0, 3],
    [70.0, 0.0, 6],
    [-70.0, 0.0, 11]
])
def test_cartesian_score(x: float, y: float, expected: int):
    """
    Check the known positions at NESW on the board have the
    expected score
    """
    assert get_score_cartesian(x, y) == expected