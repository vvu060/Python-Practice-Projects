import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fifa = pd.read_csv('F:/Python Codes/Matplotlib/fifa_data.csv')
bins = [40,50,60,70,80,90,100]
plt.title('Fifa Histogram', fontdict={'fontweight': 'bold', 'fontsize': 20})
plt.hist(fifa.Overall, bins=bins, color='#abcdef')
plt.xticks(bins)
plt.xlabel('Overall Score')
plt.ylabel('No. Of Players')


plt.show()