"""
Base file for the Utils class.
"""
from typing import Any


class Utils:
    """
    The utils class holds many abstracted bits of logic to make my life easier. These functions are all static functions
    that take in basic parameters. Most functions involve basic tuple logic for the word search grid to use.
    """
    
    @staticmethod
    def multiply_tuples(t1: tuple, t2: tuple) -> tuple[Any, ...]:
        """
        Multiplies two tuples together. (2, 3) * (2, 4) = (4, 12)
        @param t1: First given tuple
        @param t2: Second given tuple
        @return: The product of the two tuples
        """
        return tuple(a * b for a, b in zip(t1, t2))

    @staticmethod
    def multiply_tuple(t: tuple, n: float or int) -> tuple[int | Any, ...]:
        """
        Multiples a whole tuple by a number. Ex: (1, 2) * 2 = (2, 4)
        @param t: The given Tuple
        @param n: The given number that is the multiplier
        @return: The new multiplied tuple.
        """
        return tuple(i * n for i in t)

    @staticmethod
    def add_tuples(t1: tuple, t2: tuple) -> tuple:
        """
        Simply add the two integers in the two tuples together.
        @param t1: The first given tuple
        @param t2: The second given tuple
        @return: The sum of the two given tuples
        """
        return t1[0] + t2[0], t1[1] + t2[1]
