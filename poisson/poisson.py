import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
dataset = sm.datasets.get_rdataset("discoveries")
df = dataset.data.set_index("time")
df.head(10).T
fig, ax = plt.subplots(1, 1, figsize=(16, 4))
df.plot(kind='bar', ax=ax)
model = smf.poisson("discoveries ~ 1", data=df)
result = model.fit()
print(result.summary())
