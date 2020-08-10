import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fifa = pd.read_csv('F:/Python Codes/Matplotlib/fifa_data.csv')
plt.figure(figsize=(4,6))
barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
arsenal = fifa.loc[fifa.Club == 'Arsenal']['Overall']

labels = ['FC Barcelona', 'Real Madrid', 'Arsenal']
boxes = plt.boxplot([barcelona,madrid,arsenal], labels=labels, patch_artist=True, medianprops={'linewidth': 2})

for box in boxes['boxes']:
    #Set edge color
    box.set(color = '#4286f4', linewidth=2)

    #Set Fill color
    box.set(facecolor = '#e0e0e0')
plt.title("Soccer Team Comparison")
plt.ylabel('Overall Rating')
plt.xlabel('Teams')
plt.show()