import functools

def pow(a, x, b):
    """Computes a^x mod b

    Parameters
    ----------
    a: int
        Base of exponentiation
    x: int
        Exponent
    b: int
        Modulo

    Returns
    -------
    int
        a^x mod b

    """
    return functools.reduce(lambda r, _ : (r*a) % b, range(x), 1)

