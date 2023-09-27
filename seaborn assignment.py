#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Que 1: Name any five plots that we can plot using the Seaborn library. Also, state the uses of each plot.
Scatter Plot: A scatter plot is used to visualize the relationship between two variables. It is useful in determining whether the variables are correlated or not. Seaborn's scatter plot allows us to add a third variable to the plot using the hue parameter.

Line Plot: Line plots are useful for visualizing trends in data over time. Seaborn's line plot allows us to add error bars to the plot using the ci parameter.

Bar Plot: Bar plots are used to visualize categorical data. They can be used to compare the frequency of different categories or to compare a single category across different groups. Seaborn's bar plot allows us to add error bars to the plot using the ci parameter.

Histogram: A histogram is used to visualize the distribution of a single variable. It is useful in determining the shape of the distribution and presence of outliers. Seaborn's histogram allows us to add a kernel density estimate to the plot using the kde parameter.

Heatmap: Heatmaps are useful for visualizing the relationship between two variables in a matrix format. They are commonly used in exploratory data analysis to identify patterns and correlations in the data. Seaborn's heatmap allows us to customize the color map using the cmap parameter.



# Q2

# In[4]:


import seaborn as sns
fmri_data = sns.load_dataset("fmri")
sns.lineplot(x = fmri_data.timepoint , y = fmri_data.signal)


# Q3

# In[7]:


data =sns.load_dataset('titanic')
sns.boxplot(x='pclass', y = 'age', data =data)
sns.boxplot(x='pclass', y = 'fare',data =data)


# In[ ]:


Q4


# In[10]:


diamond_data =sns.load_dataset('diamonds')
sns.histplot(x='price', hue ='cut', data = diamond_data)


# Q5
# 

# In[13]:


iris_data = sns.load_dataset('iris')
sns.pairplot(data= iris_data,hue="species")


# Q6

# In[ ]:


# Load flights dataset
flights = sns.load_dataset('flights')

# Reshape data into pivot table
flights_pivot = flights.pivot('month', 'year', 'passengers')

# Plot heatmap
sns.heatmap(flights_pivot, cmap='Blues')

