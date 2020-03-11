import numpy as np

import calculate_central_tendency as my_cal


def test_get_mean():
    X = np.array([1, 2, 3, 5])

    out_expected = 2.75
    out = my_cal.get_mean(X)

    np.testing.assert_almost_equal(out, out_expected)


def test_get_median():
    X_1 = np.array([1, 2, 3, 5])
    X_2 = np.array([1, 2, 3, 5, 6])

    out_expected_1 = 2.5
    out_expected_2 = 3
    out_1 = my_cal.get_median(X_1)
    out_2 = my_cal.get_median(X_2)

    np.testing.assert_almost_equal(out_1, out_expected_1)
    np.testing.assert_almost_equal(out_2, out_expected_2)


def test_get_mode():
    X = np.array([1, 1, 2, 2, 2, 3, 3, 3, 4])

    out_expected = np.array([2, 3])
    out = my_cal.get_mode(X)

    np.testing.assert_array_equal(out, out_expected)
