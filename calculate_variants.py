"""Program generate all variants of power acting on positive charge in right triangle.

Attributes:
    prefix_nano_value (int): Value of nano prefix.
    cathets (tuple[float, float]): Cathets of triangle in meters.
    hypotenuse (float): Hypotenuse of triangle in meters.
    q1_nKL (int): Charge of positive charge in nKL.

"""

from decimal import Decimal
from typing import Generator

prefix_nano_value = 10 ** -9
cathets = (0.3, 0.4)
hypotenuse = 0.5
q1_nKL = 1


def generate_all_variants(accuracy: int) -> Generator:
    """Generates permutation variants in nKl with some accuracy.

    1 char after coma
    Examples:
        >>> list(generate_all_variants(1))
        [(-0.1, -0.9), (-0.2, -0.8), (-0.3, -0.7), (-0.4, -0.6), (-0.5, -0.5), (-0.6, -0.4), (-0.7, -0.3), (-0.8, -0.2), (-0.9, -0.1)]

    """
    q2 = step = -Decimal(str(10 ** -accuracy))
    while abs(q2) != q1_nKL:
        q3 = -(q1_nKL - abs(q2))
        yield float(q2), float(q3)
        q2 += step


def calculate_all_powers(accuracy: int = 3) -> None:
    """The function that starts the project. Calculate all powers permutations acting on positive charge.

    Note:
        Results have small margin, because float type have limited accuracy.

    """
    for q2, q3 in generate_all_variants(accuracy):
        f2, f3 = calculate_power_negative_charge(q2, q3)
        print(f'F2 (for charge {q2=}nKL) = {f2:.{accuracy}}nH, F3 (for charge {q3=}nKL) = {f3:.{accuracy}}nH')


def calculate_power_negative_charge(q2: float, q3: float) -> tuple[float, float]:
    """Calculates power acting on the positive charge behind Coulomb's law in nH.

    Args:
        q2: First negative charge in nKL.
        q3: Second negative charge in nKL.

    """
    if abs(q2 + q3) != q1_nKL:
        raise ValueError('The sum of negative charges should be equal to positive')
    k = 9 * 10 ** 9
    q1 = prefix_nano_value
    q2 *= prefix_nano_value
    q3 *= prefix_nano_value
    f2 = k * (abs(q1) * abs(q2) / (cathets[0] ** 2)) / prefix_nano_value
    f3 = k * (abs(q1) * abs(q3) / (cathets[1] ** 2)) / prefix_nano_value
    return f2, f3


if __name__ == '__main__':
    calculate_all_powers()
