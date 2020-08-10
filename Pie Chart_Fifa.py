import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fifa = pd.read_csv('F:/Python Codes/Matplotlib/fifa_data.csv')
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
labels = ['Left', 'Right']
colors = ['#abcdef', '#aabbbc']
plt.pie([left, right], labels=labels, colors=colors, autopct='%.2f %%')
plt.title("Foot Preference of Players")
plt.show()