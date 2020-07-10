# --------------------------------------------
# Exercise: polygon
# --------------------------------------------

import math

def polysum (n, s):
    '''
    Parameters
    ----------
    n : int
        the number of sides of polygon
    s : float or int
        the length of the side of polygon

    Returns sum of area and square of the perimeter of the regular polygon
    -------
    '''
    area = (0.25 * n * s * s) / (math.tan(math.pi / n))
    peri = n * s
    return round(area + peri * peri, 4)
    