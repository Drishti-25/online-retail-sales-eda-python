#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Loading Data

# In[3]:


# NOTE:
# This dataset contains non-UTF-8 characters (e.g., currency symbols).
# Using 'latin1' as a fallback encoding to prevent UnicodeDecodeError.
# If issues arise, detect encoding using chardet before loading.
# 'python' engine is more tolerant of messy CSV formatting.

df = pd.read_csv('OnlineRetail.csv', encoding='latin1', engine='python')
df.head()


# ### EDA

# In[4]:


# checking number of rows and columns

df.shape


# In[5]:


# structural information about the dataset

df.info()    #need to convert the data col type


# In[6]:


# statistical summary of numerical columns

df.describe()


# In[7]:


# converting InvoiceDate to datetime datatype
# as datetime type enables time-based operations(eg:feature extraction)

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df.info()


# In[8]:


df.columns


# ### Data cleaning

# In[9]:


# filtering dataset: keeping only records of united kingdom

df_filtered = df[(~df['InvoiceNo'].str.startswith('C')) & (df['Country'] == 'United Kingdom') ]
df_filtered


# In[10]:


# checking for missing values

df_filtered.isnull().sum()


# In[11]:


# dropping records with null customer ids
# also the nulls in product description

df_filtered = df_filtered.dropna(subset=['CustomerID'])
df_filtered = df_filtered.dropna(subset=['Description'])
df_filtered


# In[12]:


df_filtered.isnull().sum()


# In[13]:


# checking for duplicate rows

df_filtered.duplicated().sum()


# In[14]:


# removing duplicate rows

df_filtered.drop_duplicates(inplace=True)
df_filtered


# In[15]:


df_filtered = df_filtered[df_filtered['Quantity']>0]
df_filtered = df_filtered[df_filtered['UnitPrice']>0]
df_filtered


# ### Feature Engineering

# In[16]:


df_filtered['TotalRevenue'] = df_filtered['Quantity']*df_filtered['UnitPrice']
df_filtered


# In[17]:


df_filtered['Year'] = df_filtered['InvoiceDate'].dt.year
df_filtered['Month'] = df_filtered['InvoiceDate'].dt.month
df_filtered['Day'] = df_filtered['InvoiceDate'].dt.day
df_filtered['Hour'] = df_filtered['InvoiceDate'].dt.hour
df_filtered


# In[ ]:





# ### Analysis

# In[19]:


import duckdb


# ##### Top 10 Best selling products

# In[20]:


# Top 10 Best selling products

q1 = '''
select Description, sum(Quantity) as 'Total_quantity'
from df_filtered
group by Description
order by Total_quantity desc 
limit 10
'''

res1_df = duckdb.sql(q1).df()
res1_df.index = res1_df.index+1

res1_df


# In[62]:


# Bar chart


plt.figure(figsize=(10,7))

plt.bar(res1_df['Description'],
        res1_df['Total_quantity'])

plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.title("Top 10 Bestselling Products (UK)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ##### Top 10 Revenue products

# In[23]:


# Top 10 Revenue products

q2 = '''
select Description, sum(TotalRevenue) as 'Total_revenue'
from df_filtered
group by Description
order by Total_revenue desc 
limit 10
'''

res2_df = duckdb.sql(q2).df()
res2_df.index = res2_df.index+1

res2_df


# In[61]:


# bar chart

plt.figure(figsize=(10,7))

plt.bar(res2_df['Description'],
        res2_df['Total_revenue'])

plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Top 10 Revenue Products (UK)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ##### Sales by hour

# In[41]:


# Sales by hour

q3 = '''
select Hour, sum(TotalRevenue) as Total_revenue
from df_filtered
group by Hour
order by Hour
'''

res3_df = duckdb.sql(q3).df()
res3_df.index = res3_df.index+1

res3_df


# In[43]:


# line chart

plt.figure(figsize=(10,7))

plt.bar(res3_df['Hour'], res3_df['Total_revenue'])

plt.xlabel("Hour of Day")
plt.ylabel("Total Revenue")
plt.title("Sales Revenue by Hour")

plt.xticks(range(0,24))
plt.show()


# ##### Sales by day of week

# In[34]:


df_filtered['DayName'] = df_filtered['InvoiceDate'].dt.day_name()
df_filtered


# In[47]:


# Sales by Day of Week


q4 = '''
select DayName, sum(TotalRevenue) as 'Total_revenue'
from df_filtered
group by DayName
'''

res4_df = duckdb.sql(q4).df()
res4_df.index = res4_df.index+1

day_order = [
    "Monday","Tuesday","Wednesday",
    "Thursday","Friday","Saturday","Sunday"
]

res4_df['DayName'] = pd.Categorical(
    res4_df['DayName'],
    categories=day_order,
    ordered=True
)

res4_df = res4_df.sort_values('DayName')

res4_df


# In[50]:


# line chart

plt.figure(figsize=(5,5))

plt.bar(res4_df['DayName'], res4_df['Total_revenue'])

plt.xlabel("Day of Week")
plt.ylabel("Total Revenue")
plt.title("Sales Revenue by Day of Week")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# ##### Sales by Month

# In[54]:


df_filtered['Month'] = df_filtered['InvoiceDate'].dt.month_name()
df_filtered


# In[58]:


# sales by month

q5 = '''
select Month, sum(TotalRevenue) as 'Total_revenue'
from df_filtered
group by Month
'''

res5_df = duckdb.sql(q5).df()
res5_df.index = res5_df.index+1

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

res5_df['Month'] = pd.Categorical(
    res5_df['Month'],
    categories=month_order,
    ordered=True
)

res5_df = res5_df.sort_values('Month')

res5_df


# In[60]:


# bar chart

plt.figure(figsize=(7,5))

plt.bar(res5_df['Month'], res5_df['Total_revenue'])

plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.title('Sales Revenue by Month')


plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

