import numpy as np
from sklearn.metrics import r2_score

import calculate_determination_coefficient as my_cal


def test_calculate_covariance():
    Y_true = np.array([3, -0.5, 2, 7])
    Y_pred = np.array([2.5, 0.0, 2, 8])

    out_expected = r2_score(Y_true, Y_pred)
    out = my_cal.get_r2_score(Y_true, Y_pred)

    np.testing.assert_almost_equal(out, out_expected)
