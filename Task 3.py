#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv('C:\\Users\\mrvip\\Downloads\\householdtask3.csv')


# In[3]:


data.head(10)


# In[4]:


#scatter plot with year against own
plt.scatter(data['year'],data['own'])

#adding title to the plot
plt.title("Satter plot")

#Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[5]:


#Line chart with year again own
plt.plot(data['year'])
plt.plot(data['own'])

#adding title to the plot
plt.title("Line chart")

#Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[6]:


#Bar chart
plt.bar(data['year'],data['own'])

#adding title to the plot
plt.title("Bar chart")

#Setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')

#Showing the result
plt.show()


# In[7]:


#Histogram
plt.hist(data['income'])

plt.title('Histogram')

plt.show()


# In[ ]:




