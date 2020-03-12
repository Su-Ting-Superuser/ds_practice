import numpy as np


def get_mean(X: np.array):
    """
    calculate the mean value of the variable

    avg = sum(X) / X.size

    Args:
        X(np.array): array of numerical values

    Returns:
        avg(np.float): mean value of the variable
    """
    avg = np.sum(X) / X.size

    return avg



def get_median(X: np.array):
    """
    return the median value of the variable

    Sort X
    n is the total number of values X
    when n is odd:
        me = X[(n - 1) / 2]
    when n is even:
        me = numpy.mean(X[(n / 2) - 1], X[n / 2])

    Args:
        X(np.array): array of numerical values

    Returns:
        me(np.float): median value of the variable
    """

    me = None
    n = X.size
    X = np.sort(X)
    # if the size of X is even
    if n % 2 == 0:
        _middle_two = [X[int(n / 2 - 1)], X[int(n / 2)]]
        me = np.mean(_middle_two)
    # if the size of X is odd
    if n % 2 != 0:
        me = X[int((n - 1) / 2)]
    return me

def get_mode(X: np.array):
    """
    return the value with the highest frequency

    e.g. given [1, 1, 2, 2, 2, 3, 3, 3, 4]
    we generate it's frequency diction
    frequency_dictionary = {1: 2, 2: 3, 3: 3, 4: 1}

    mo = [2, 3]

    Args:
        X(np.array): array of numerical values

    Returns:
        mo(np.array): array of the most popular value(s)
    """
    #  TODO:  Code here
    mo = None

    return mo
