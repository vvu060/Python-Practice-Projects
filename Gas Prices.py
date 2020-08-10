import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gas = pd.read_csv('F:/Python Codes/Matplotlib/gas_prices.csv')
plt.figure(figsize=(8,5), dpi=150)
plt.title('Gas Prices in USD', fontdict={'fontweight': 'bold', 'fontsize': 20})
plt.plot(gas.Year, gas.USA, 'b.-', label='USA')
plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-', label='South Korea')
plt.plot(gas.Year, gas.Australia, 'y.-', label='Australia')

#Another way to do the same
'''for country in gas:
    if country != 'Year':
        plt.plot(gas.Year, gas[country], marker = '.')
'''

plt.xlabel("Year")
plt.ylabel("USD")
#print(gas.Year)
plt.xticks(gas.Year[::3].tolist()+[2011])
plt.legend()
plt.savefig('F:/Python Codes/Matplotlib/gas_prices.png', dpi = 300)
plt.show()