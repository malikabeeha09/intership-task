 **Energy Consumption Time Series Forecasting**

Forecast short-term household energy usage using historical time-based patterns.

**Steps Performed**

Data Preparation

Parsed datetime column and set it as index.

Resampled data to hourly averages.

Handled missing values.

Feature Engineering

Extracted hour, dayofweek, and month from datetime for ML models.

Models Implemented

ARIMA → Captures time-based trends and seasonality.

Random Forest Regressor → Machine learning model using engineered features.

Evaluation Metrics

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

Visualization

Compared Actual vs. Forecasted energy consumption.

Plotted forecasts from ARIMA and Random Forest models.

**Skills Gained**

Time series forecasting

Temporal feature engineering

Model comparison and evaluation

Visualization of time-based data
