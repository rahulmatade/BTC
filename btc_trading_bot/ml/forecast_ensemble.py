import numpy as np

def ensemble_forecast(arima_f, exp_f):
    return np.mean([arima_f, exp_f], axis=0)
