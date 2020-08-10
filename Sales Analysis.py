import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#Merge all data frames into a single file/data frame
'''
df = pd.read_csv('F:/Python Codes/Numpy/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/Sales_April_2019.csv')
files = [file for file in os.listdir('F:/Python Codes/Numpy/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data')]
all_months_data = pd.DataFrame()
for file in files:
    df = pd.read_csv('F:/Python Codes/Numpy/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/' + file)
    all_months_data = pd.concat([all_months_data,df])

all_months_data.to_csv('F:/Python Codes/Numpy/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/all_data.csv', index=False)
'''

# Read New data
all_data = pd.read_csv('F:/Python Codes/Numpy/Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data/all_data.csv')

# Identifying and Removing NaN/blank rows
nan_df = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')
#print(all_data.head())



# Identifying and Removing repeated header rows rows
all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

# Convert Columns to correct type
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

# Augment data with new columns
#Adding a Month column
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')
#print(all_data.head())

# Add a Sales Column
all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
#print(all_data.head())

# Add a City & State Column
def get_state(address):
    return address.split(',')[2].split(' ')[1]

all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1] + ' (' + get_state(x) + ')')
#Same Using f string
#all_data['City/State'] = all_data['Purchase Address'].apply(lambda x: f"{x.split(',')[1]} ({get_state(x)})")


result = all_data.groupby('City').sum()
#print(result)

# Q1: Best and Worst Sales month
'''
months = range(1,13)
plt.bar(months,result['Sales'])
plt.title('Monthly Sales')
plt.xticks(months)
plt.xlabel('Month Number')
plt.ylabel('Sales in USD')
plt.show()
'''
# Q2: Which City has highest sales
'''
cities = [city for city, df in all_data.groupby('City')]
plt.bar(cities, result['Sales'])
plt.title('City Sales')
plt.xticks(cities, rotation='vertical', size = 8)
plt.xlabel('City Name')
plt.ylabel('Sales in USD')
plt.show()
'''

# Q3: What time should the ads be displayed to maximize sales
'''
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute
#print(all_data.head())

hours = [hour for hour, df in all_data.groupby('Hour')]
plt.plot(hours, all_data.groupby(['Hour']).count())
plt.title('Order Time by Hour')
plt.xticks(hours)
plt.xlabel('Hours')
plt.ylabel('No. of Orders')
plt.grid()
plt.show()'''

# Q4: What Products are sold together
'''
df = all_data[all_data['Order ID'].duplicated(keep=False)]
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df = df[['Order ID','Grouped']].drop_duplicates()
#print(df.head())

from itertools import combinations
from collections import Counter

count = Counter()
for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))

for key, value  in count.most_common(10):
    print(key, value)'''

# Q5: What product is ordered the most?

product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']
products = [product for product, df in product_group]
'''plt.bar(products, quantity_ordered)
plt.xticks(products,  rotation='vertical', size = 6)
plt.ylabel('# Ordered')
plt.xlabel('Products')
plt.title("Product Sales")
plt.show()
'''
prices = all_data.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.bar(products, quantity_ordered)
ax2.plot(products, prices, 'r-')
ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color = 'r')
ax1.set_ylabel('Prices', color = 'b')
ax1.set_xticklabels(products, rotation='vertical', size = 6)
plt.show()

