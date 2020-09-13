#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[8]:


x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])
plt.show()


# In[10]:


sample_data = pd.read_csv('sample_data.csv')


# In[11]:


sample_data


# In[12]:


type(sample_data)


# In[14]:


sample_data.column_c.iloc[0]


# In[16]:


plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c, 'o')
plt.show()


# In[17]:


data = pd.read_csv('countries.csv')


# In[18]:


data


# In[19]:


us = data[data.country == "United States"]


# In[21]:


china = data[data.country == 'China']


# In[22]:


china


# In[26]:


plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()


# In[ ]:


plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()

