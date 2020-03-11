import numpy as np

import calculate_cov_and_corr as my_cal


def test_calculate_covariance():
    X = np.array([1, 2, 3])
    Y = np.array([6, 1, -4])

    out_expected = -10 / 3
    out = my_cal.get_covariance(X, Y)

    np.testing.assert_almost_equal(out, out_expected)


def test_get_pearson_correlation_coefficient():
    X = np.array([1, 2, 3])
    Y = np.array([6, 1, 4])

    #  np.corrcoef returns a correlation metric
    #  where the values on top_left-bottom_right diagnose is always 1
    out_expected = np.corrcoef(X, Y)[0][1]
    out = my_cal.get_pearson_correlation_coefficient(X, Y)

    np.testing.assert_almost_equal(out, out_expected)
