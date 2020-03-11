import numpy as np


def get_r2_score(Y: np.array, Y_pred: np.array):
    """
    calculate the coefficient of determination(r2) of the regression

    SStot = sum[(y - y_bar) ^ 2]
    SSreg = sum[(y_pred - y_bar) ^ 2]
    SSres = sum[(y - y_pred) ^ 2]

    r2 = 1 - SSres / SStot

    Args:
        Y(np.array): array of the true values
        Y_pred(np.array): array of the predicted values

    Returns:
        r2(np.float): coefficient of determination
    """
    y_bar = np.mean(Y)
    SStot = np.sum(np.square(Y - y_bar))
    SSres = np.sum(np.square(Y - Y_pred))

    r2 = 1 - SSres / SStot

    return r2
