#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('C:\\Users\\mrvip\\Downloads\\01.Data Cleaning and Preprocessing.csv')


# In[3]:


type(data)


# In[4]:


data.info


# In[5]:


data.describe()


# In[8]:


data = data.drop_duplicates()
data


# In[9]:


data.isnull()


# In[10]:


data.isnull().sum()


# In[11]:


data.notnull()


# In[12]:


data.isnull().sum().sum()


# In[13]:


data2 = data.fillna(value=0)
data2


# In[14]:


data3 = data.fillna(method='pad')
data3


# In[15]:


data4 = data.fillna(method='bfill')
data4


# In[16]:


import numpy as np
from scipy import stats


# In[17]:


data2.columns


# In[18]:


data2.drop(['Observation'], axis=1, inplace=True)

data2.columns


# In[20]:


Q1 = data2.quantile(0.25)

Q3 = data2.quantile(0.75)

IQR=Q3-Q1

print(IQR)


# In[22]:


data2 = data2[-((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]

data2


# In[23]:


data2.describe()


# In[ ]:




