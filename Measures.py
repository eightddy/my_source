__author__ = 'MAHMADI'

import numpy as np
import sys

def multiclass_log_loss(y_true, y_pred, eps=1e-15):
    print y_true
    print y_pred
    predictions = np.clip(y_pred, eps, 1 - eps)
    print predictions.sum(axis=1)[:, np.newaxis]
    predictions /= predictions.sum(axis=1)[:, np.newaxis]
    print predictions
    actual = np.zeros(y_pred.shape)
    print actual
    sys.exit()
    rows = actual.shape[0]
    actual[np.arange(rows), y_true.astype(int)-1] = 1
    #vsota = np.sum(actual * np.log(predictions)+(1-actual)*np.log(1-predictions))
    vsota = np.sum(actual * np.log(predictions))
    return -1.0 / rows * vsota