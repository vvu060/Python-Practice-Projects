#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


# # Load csv file into memory

# In[4]:


data = pd.read_csv('F:/Python Codes/Numpy/uber-raw-data-apr14.csv')
data.head()


# In[5]:


dt = '4/1/2014 0:11:00'
dt = pd.to_datetime(dt)


# In[7]:


data['Date/Time'] = data['Date/Time'].map(pd.to_datetime)


# In[8]:


data.tail()


# # Adding useful Columns

# In[9]:


def get_dom(dt):
    return dt.day

data['dom'] = data['Date/Time'].map(get_dom)


# In[17]:


def get_weekday(dt):
    return dt.weekday()

data['Weekday'] = data['Date/Time'].map(get_weekday)


# In[18]:


def get_hour(dt):
    return dt.hour

data['Hour'] = data['Date/Time'].map(get_hour)


# In[19]:


data.tail()


# # Analysis

# In[ ]:


#Frequency by DOM Uber April 2014


# In[35]:


plt.hist(data.dom, bins=30, rwidth=0.8, range=(0.5,30.5))
plt.title('Frequency by DOM Uber April 2014')
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.show()


# In[42]:


def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date_sorted = by_date.sort_values()


# In[47]:


plt.bar(range(1,31), by_date_sorted)
plt.xticks(range(1,31), by_date_sorted.index)
plt.title('Frequency by DOM Uber April 2014')
plt.xlabel('Days')
plt.ylabel('Frequency')
plt.show()


# # Analyse by Weekdays

# In[50]:


plt.hist(data.Weekday, bins=7, range=(-0.5,6.5), rwidth=0.8, color='g', alpha=0.4)
plt.xticks(range(7), 'Mon,Tue,Wed,Thu,Fri,Sat,Sun'.split(','))
plt.show()


# # Cross Analysis (Hour, DOW)

# In[53]:


by_cross = data.groupby('Weekday Hour'.split()).apply(count_rows).unstack()


# In[54]:


sb.heatmap(by_cross)


# # By Lon & Lat

# In[58]:


plt.hist(data['Lon'], bins=100, range=(-74.2,-73.7))
("")


# In[67]:


plt.hist(data['Lat'], bins=100, range=(40.5,40.9))
("")


# In[70]:


plt.hist(data['Lon'], bins=100, range=(-74.2,-73.7), color='g', alpha=0.5, label = 'Longitude')
plt.legend(loc='upper left')
plt.twiny()
plt.hist(data['Lat'], bins=100, range=(40.5,40.9), color='r', alpha=0.5, label = 'Latitude')
plt.legend(loc='best')
("")


# # Map

# In[73]:


plt.figure(figsize=(15,15))
plt.plot(data['Lon'],data['Lat'], '.', ms=1)
plt.xlim(-74.2,-73.7)
plt.ylim(40.5,40.9)
("")

