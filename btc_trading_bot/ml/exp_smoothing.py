from statsmodels.tsa.holtwinters import ExponentialSmoothing

def exp_smooth_forecast(series, steps=5):
    model = ExponentialSmoothing(series, trend="add")
    fitted = model.fit()
    return fitted.forecast(steps)
