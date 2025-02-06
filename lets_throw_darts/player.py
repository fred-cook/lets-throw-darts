from dataclasses import asdict

import numpy as np

from lets_throw_darts.coord_converter import circ_to_cart
from lets_throw_darts.checkouts import checkout_lookup
from lets_throw_darts.score import get_score_cartesian
from lets_throw_darts.segment_centres import targets

class BasicPlayer:
    """
    A basic darts player that scores as high as it can (T20)
    or goes for a checkout if one is present

    x_sigma and y_sigma are in mm
    """
    def __init__(self, name: str,  x_sigma: float, y_sigma: float):
        self.name = name
        self.x_sigma = x_sigma
        self.y_sigma = y_sigma
        self.noise = np.array([x_sigma, y_sigma])

        self.score = 501
        self.total_darts = 0

    def take_turn(self) -> bool:
        """
        Take a turn of throwing 3 darts at the board

        Returns
        -------
        bool
            True if player has won
        """
        print(f"{self.name} to throw, total: {self.score}")
        start_score = self.score
        darts = 3
        
        for dart in range(darts):
            self.total_darts += 1
            checkout = checkout_lookup.get(str(self.score), None)

            if checkout is None:
                # aim for max score
                target = "T20"
            else:
                target = checkout[0]

            score = self.throw_dart(target)
            print(f"\tdart {dart + 1}: score {score:2d} (aimed for {target})")
            self.score -= score

            if self.score == 0:
                print(f"{self.name} checks out with {target} after {self.total_darts} darts")
                return True
            if self.score < 2:
                print("BUST")
                self.score = start_score
                return False
        return 
    
    def throw_dart(self, target: str) -> int:
        """
        Throw a dart with added noise

        Parameters
        ----------
        target: str
            S/D/T + number, or Bull/Outer
        """
        noise_x, noise_y = np.random.randn(2) * self.noise
        x, y = circ_to_cart(**asdict(targets[target]))
        return get_score_cartesian(x=x + noise_x, y= y + noise_y)


if __name__ == "__main__":
    player = BasicPlayer("Fred", 5.0, 5.0)

    while 1:
        if player.take_turn():
            break