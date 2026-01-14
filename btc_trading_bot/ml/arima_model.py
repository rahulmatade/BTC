from statsmodels.tsa.arima.model import ARIMA

def arima_forecast(series, steps=5):
    model = ARIMA(series, order=(2,1,2))
    fitted = model.fit()
    return fitted.forecast(steps=steps)
