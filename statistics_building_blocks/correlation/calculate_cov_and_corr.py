import numpy as np


def get_covariance(X: np.array, Y: np.array):
    """
    calculate covariance(cov) of two variables X and Y

    cov(X, Y) = E[(X - E[X])(Y - E[Y])]
    cov(X, Y) = E[XY] - E[X]E[Y]

    Args:
        X(np.array): array of numerical values
        Y(np.array): array of numerical values

    Returns:
        cov(np.float): covariance of the two variables
    """
    mean_of_X = np.mean(X)
    mean_of_Y = np.mean(Y)
    mean_of_XY = np.mean(X * Y)

    cov = mean_of_XY - mean_of_X * mean_of_Y

    return cov


def get_pearson_correlation_coefficient(X: np.array, Y: np.array):
    """
    calculate the pearson correlation coefficient(r) of two variables X and Y

    r = cov(X, Y) / (std(X) * std(Y))

    where cov is the covariance, std is the standard deviation

    Args:
        X(np.array): array of numerical values
        Y(np.array): array of numerical values

    Returns:
        r(np.array): pearson correlation coefficient of the two variables, -1 <= r <= 1
    """
    cov = get_covariance(X, Y)
    std_X = np.std(X)
    std_Y = np.std(Y)

    r = cov / (std_X * std_Y)

    return r
