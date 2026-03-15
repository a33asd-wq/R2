"""
https://en.wikipedia.org/wiki/Fahrenheit
https://en.wikipedia.org/wiki/Celsius
"""


def fahrenheit_to_celsius(temp: float) -> float:
    """
    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(39)
    3.89
    """
    temp -=32
    return round(5 * temp / 9, 2)


def celsius_to_fahrenheit(tempr: float) -> float:
    """
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(30.5)
    86.9
    """
    tempr *= 9/5
    return round((tempr * 9 / 5) + 32, 2)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    # rg 
