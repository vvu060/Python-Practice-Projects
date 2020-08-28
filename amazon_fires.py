import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

amazon_fires = pd.read_csv("amazon.csv", encoding= 'ISO-8859-1')




amazon_fires['number'] = amazon_fires['number'].apply(np.round)
#print(amazon_fires.head(10))
#print(amazon_fires.describe())

print(amazon_fires['year'].min())
print(amazon_fires['year'].max())

amazon_acre = amazon_fires['state'] == 'Acre'
amazon_acre_data = amazon_fires[amazon_acre]
#print(amazon_acre_data.describe())
amazon_acre_number = amazon_acre_data['number']
print(amazon_acre_number.sum())

# Number of Fires by year
acre_fires_year= amazon_fires[amazon_fires['state'] == 'Acre'].groupby('year').sum()
acre_fires_year.reset_index(inplace=True)
print(acre_fires_year.head())

fig = plt.figure(figsize=(12,5))
sns.barplot(x='year', y = 'number', data=acre_fires_year)
#plt.show()


# Number of Fires by State
total_fires = amazon_fires.groupby('state')['number'].sum().reset_index()
#print(total_fires)
fig1 = plt.figure(figsize=(12,5))
t = sns.barplot(x='state', y = 'number', data=total_fires)
t.set_xticklabels(t.get_xticklabels(), rotation =45, horizontalalignment='right')
plt.show()

# Number of Fires in 2017
total_fires_2017 = amazon_fires[amazon_fires['year'] == 2017][['number','month']].groupby('month').sum().reset_index()
fig2 = plt.figure(figsize=(12,5))
m = sns.barplot(x='month', y='number', data=total_fires_2017)
m.set_xticklabels(m.get_xticklabels(), rotation =45, horizontalalignment='right')
plt.show()

#States where fires occurred in ‘December’ month
dec_fires = amazon_fires[amazon_fires['month'] == 'Dezembro']['state'].unique()
print("Below are the states where fire occured in December: \n{}".format(dec_fires))
