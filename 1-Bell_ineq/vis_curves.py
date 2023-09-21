# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('scandic')

cal_1 = 32
cal_0 = 2

# read the data
arm_1 = pd.read_csv('curve_1.csv', skiprows=2, sep=";").to_numpy()
arm_1[:, 0] = arm_1[:, 0] - cal_1

arm_0 = pd.read_csv('curve_2.csv', skiprows=2, sep=";").to_numpy()
arm_0[:, 0] = arm_0[:, 0] - cal_0

# %%
plt.figure(figsize=(5, 2.6))
plt.plot(arm_1[:, 0], arm_1[:, 1], '.-', label='arm 1')
plt.plot(arm_0[:, 0], arm_0[:, 1], '.-', label='arm 0')
plt.xlabel('angle [deg]')
plt.ylabel('counts')
plt.xticks(np.arange(0, 240, 45))
plt.legend()

# %%
