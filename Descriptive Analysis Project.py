#!/usr/bin/env python
# coding: utf-8

# In[59]:


#Imports all the libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[60]:


# Import Warnings packages to ignore the warning messages
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)


# In[61]:


#Add database file
DF=pd.read_csv("F500.csv")


# In[62]:


#Find the shape of data set
DF.shape
DF.dtypes
DF.isnull().sum()


# In[63]:


# Print the 5 columns in dataset

DF.head()


# In[91]:


print(DF.dtypes)
#Summary of data set
df=pd.DataFrame(DF)
summary=df.info()
print(summary)


# In[65]:


df.isnull()


# In[66]:


data = {
    'Year': [1955, 1967, 1980, 1993, 2005],
    'Rank': [1, 125.75, 250.5, 375.25, 500],
    'Revenue (in millions)': [49.7, 362.3, 1019, 3871, 288189]
}
df = pd.DataFrame(data)

# Step 3: Use the describe() function
description = df.describe()

# Step 4: Calculate IQR
description.loc['IQR'] = description.loc['75%'] - description.loc['25%']

# Display the results
print(description)


# In[67]:


data = {
    'Company': ['CBS', 'NBC', 'FOX', 'CBS', 'ABC', 'CBS', 'FOX', 'N.A.'],
    'Profit (in millions)': ['100', '150', '200', 'N.A.', '300', '400', 'N.A.', '500']
}

df = pd.DataFrame(data)
description = df.describe(include='object')
print(description)


# In[68]:


data = {
     'Year': [1955, 1967, 1980, 1993, 2005,2007,2008,1995],
    'Rank': [1, 125.75, 250.5, 375.25, 500,144,250,375],
    'Revenue (in millions)': [49.7, 362.3, 1019, 3871, 288189,362,11351,88497],
    'Company': ['CBS', 'NBC', 'FOX', 'CBS', 'ABC', 'CBS', 'N.A.','ABC'],
    'Profit (in millions)': ['100', '150', '200', 'N.A.', '300', '400', 'N.A.', '500']
}

df = pd.DataFrame(data)
summary_all=df.describe(include='all')
print(summary_all)


# In[69]:


# Mean of revenue in million
mean_revenue = df['Revenue (in millions)'].mean()
print(f"Mean: {mean_revenue}")

# Median of revenue in million
median_revenue = df['Revenue (in millions)'].median()
print(f"Median: {median_revenue}")

# Mode of revenue in million
mode_revenue = df['Revenue (in millions)'].mode()
print(f"Mode: {mode_revenue[0]}")


# In[70]:


data = df['Revenue (in millions)']

sns.distplot(data, bins=10, hist=True, kde=True, label = 'Revenue (in millions)')


# In[71]:


# Minimum value
min_revenue = df['Revenue (in millions)'].min()
print(f"Minimum: {min_revenue}")

# Maximum value
max_revenue = df['Revenue (in millions)'].max()
print(f"Maximum: {max_revenue}")

# Range
range_revenue = max_revenue - min_revenue
print(f"Range: {range_revenue}")

# Variance
variance_revenue = df['Revenue (in millions)'].var()
print(f"Variance: {variance_revenue}")

# Standard Deviation
std_dev_revenue = df['Revenue (in millions)'].std()
print(f"Standard Deviation: {std_dev_revenue}")

# Interquartile Range (IQR)
Q1 = df['Revenue (in millions)'].quantile(0.25)
Q3 = df['Revenue (in millions)'].quantile(0.75)
IQR = Q3 - Q1
print(f"Interquartile Range (IQR): {IQR}")


# In[72]:


df.hist(figsize=(10,12))
plt.show()


# In[73]:


df.skew(numeric_only=True)


# In[74]:


#Check boxplot of revenue in million
plt.figure(figsize=(10, 6))
sns.boxplot(y=df['Revenue (in millions)'])
plt.title('Boxplot of Revenue (in millions)')
plt.ylabel('Revenue (in millions)')
plt.show()


# In[75]:


#Compute the skewness of revenue in million
skewness = df['Revenue (in millions)'].skew()
print(f"Skewness: {skewness}")


# In[76]:


#Compute the kurtosis of revenue in million
kurtosis=df['Revenue (in millions)'].kurt()
print(f"kurtosis:{kurtosis}")


# In[89]:


#Cheack the valuecount of revenue in million
value_counts = df['Revenue (in millions)'].value_counts()
print(value_counts)


# In[86]:


df["Profit (in millions)"] = df["Profit (in millions)"].replace('N.A', 0)
df.describe()


# In[87]:


df["Profit (in millions)"] = pd.to_numeric(df["Profit (in millions)"], errors='coerce')


# In[ ]:




