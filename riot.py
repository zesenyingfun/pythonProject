from polygon import RESTClient
import mplfinance as mpf
import pandas as pd
import numpy as np
import datetime as dt
import requests
from matplotlib import pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller


client = RESTClient("2zH7AFDp4wW1Uqov4zGvbpA2aUNHbk__adRrOG")  # POLYGON_API_KEY environment variable is used

# make request
request = client.get_daily_open_close_agg(
    "AAPL",
    "2023-02-07",
)
print(request)