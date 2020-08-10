import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fifa = pd.read_csv('F:/Python Codes/Matplotlib/fifa_data.csv')
fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]
plt.style.use('ggplot')

light = fifa.loc[fifa.Weight < 140].count()[0]
medium = fifa.loc[(fifa.Weight >= 140) & (fifa.Weight < 175)].count()[0]
heavy = fifa.loc[fifa.Weight >= 175].count()[0]
weights = [light, medium, heavy]
labels = ['Under 140', '140-175', 'Over 175']
explode = [0.1,0,0]
plt.pie(weights, labels=labels, autopct='%.2f %%', pctdistance=0.8, explode=explode)
plt.title('Weight Distribution of Players in Fifa (lbs)')
plt.show()