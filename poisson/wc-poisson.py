import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import Series
from pandas import read_csv
from pandas import DataFrame

series = read_csv('wc98_workload_hour.csv', header=0, parse_dates=[0], index_col=0, squeeze=True)
df = DataFrame(series)
fig, ax = plt.subplots(1, 1)
df.plot(kind='bar', ax=ax)
model = smf.poisson("count ~ 1", data=df)
result = model.fit()
print(result.summary())
