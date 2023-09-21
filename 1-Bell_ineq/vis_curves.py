# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('scandic')

# read the data
data = pd.read_csv('curve_1.csv', skiprows=2, sep=";").to_numpy()
# %%
plt.plot(data[:, 0], data[:, 1], '.-', label='arm 1')
# %%
