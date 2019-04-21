#Excercise 6

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#NumPy and Matplotlib
#Q1
"""
t = np.arange(-1, 1.1, 0.1)
y1 = np.arcsin(t)
y2 = np.arccos(t)
plt.plot(t, y1, color='r', marker='x', label ="arcsin")
plt.plot(t, y2, color='b', marker='o', label ="arccos")
plt.legend()
plt.show()
"""

#Pandas and Matplotlib
#Q1
"""
filename = ("AID_1053208_datatable_all.csv")
data = pd.read_csv(filename)

PB_activity = data['PUBCHEM_ACTIVITY_OUTCOME']
Fold_change = data['FOLD_CHANGE_RATIO']

t = np.arange(0, len(data), 1)
plt.scatter(t, Fold_change, label ="Fold")
plt.legend()
plt.ylabel("Gene Number")
plt.xlabel("Fold Change Ratio")
plt.title("Fold Change Ratio and Gene Number")

plt.show()
"""

"""
filename = ("AID_1053208_datatable_all.csv")
data = pd.read_csv(filename)

PB_activity = data['PUBCHEM_ACTIVITY_OUTCOME']
Fold_change = data['FOLD_CHANGE_RATIO']

print(PB_activity)

PB_Active = (PB_activity == "Active")
PB_Inactive = (PB_activity == "Inactive")

t = np.arange(0, len(data), 1)
plt.scatter(t, Fold_change, label ="Fold")
plt.scatter(t, PB_Active, color='r', marker='x', label ="Active")
plt.scatter(t, PB_Inactive, color='b', marker='o', label ="Inactive")

plt.legend()
plt.ylabel("Gene Number")
plt.xlabel("Fold Change Ratio")
plt.title("Fold Change Ratio and Gene Number")

plt.show()
"""
















