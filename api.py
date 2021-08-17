#!/usr/bin/env python
# coding: utf-8

# This exercise will require you to pull some data from the Qunadl API. Qaundl is currently the most widely used aggregator of financial market data.

# As a first step, you will need to register a free account on the http://www.quandl.com website.

# After you register, you will be provided with a unique API key, that you should store:

# In[51]:


# Store the API key as a string - according to PEP8, constants are always named in all upper case
API_KEY = 'ggjDohkWphxEPY1AjbER'


# Qaundl has a large number of data sources, but, unfortunately, most of them require a Premium subscription. Still, there are also a good number of free datasets.

# For this mini project, we will focus on equities data from the Frankfurt Stock Exhange (FSE), which is available for free. We'll try and analyze the stock prices of a company called Carl Zeiss Meditec, which manufactures tools for eye examinations, as well as medical lasers for laser eye surgery: https://www.zeiss.com/meditec/int/home.html. The company is listed under the stock ticker AFX_X.

# You can find the detailed Quandl API instructions here: https://docs.quandl.com/docs/time-series

# While there is a dedicated Python package for connecting to the Quandl API, we would prefer that you use the *requests* package, which can be easily downloaded using *pip* or *conda*. You can find the documentation for the package here: http://docs.python-requests.org/en/master/ 

# Finally, apart from the *requests* package, you are encouraged to not use any third party Python packages, such as *pandas*, and instead focus on what's available in the Python Standard Library (the *collections* module might come in handy: https://pymotw.com/3/collections/ ).
# Also, since you won't have access to DataFrames, you are encouraged to us Python's native data structures - preferably dictionaries, though some questions can also be answered using lists.
# You can read more on these data structures here: https://docs.python.org/3/tutorial/datastructures.html

# Keep in mind that the JSON responses you will be getting from the API map almost one-to-one to Python's dictionaries. Unfortunately, they can be very nested, so make sure you read up on indexing dictionaries in the documentation provided above.

# In[52]:


# First, import the relevant modules
import json
import requests 
import pandas as pd


# Note: API's can change a bit with each version, for this exercise it is reccomended to use the "V3" quandl api at `https://www.quandl.com/api/v3/`

# In[53]:


# Now, call the Quandl API and pull out a small sample of the data (only one day) to get a glimpse
# into the JSON structure that will be returned
url = 'https://www.quandl.com/api/v3/datasets/FSE/AFX_X?start_date=2017-01-01&end_date=2017-12-31&api_key' + API_KEY
r = requests.get(url)
json_data = r.json()


# In[54]:


# Inspect the JSON structure of the object you created, and take note of how nested it is,
# as well as the overall structure
#json_data['dataset']['data']


# These are your tasks for this mini project:
# 
# 1. Collect data from the Franfurt Stock Exchange, for the ticker AFX_X, for the whole year 2017 (keep in mind that the date format is YYYY-MM-DD).
# 2. Convert the returned JSON object into a Python dictionary.
# 3. Calculate what the highest and lowest opening prices were for the stock in this period.
# 4. What was the largest change in any one day (based on High and Low price)?
# 5. What was the largest change between any two days (based on Closing Price)?
# 6. What was the average daily trading volume during this year?
# 7. (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

# In[55]:


open_index = json_data['dataset']['column_names'].index('Open')


# In[56]:


json_data['dataset']['data'][0][1]


# ### Calculate what the highest and lowest opening prices were for the stock in this period.

# In[57]:


list_open=[]
for i in json_data['dataset']['data']:
    list_open.append(i[1])


# In[58]:


list_open = [a for a in list_open if a is not None]

print('The highest opening price was:',max(list_open))
print('The lowest opening price was:',min(list_open))


# ### What was the largest change in any one day (based on High and Low price)?

# In[59]:


high_index = json_data['dataset']['column_names'].index('High')
high_index


# In[60]:


low_index = json_data['dataset']['column_names'].index('Low')
low_index


# In[61]:


dailychange = []

for i in json_data['dataset']['data']:
    diff = i[high_index] - i[low_index]
    dailychange.append(diff)


# In[62]:


#dailychange


# In[63]:


print('The largest change in one day (based on High and Low price)',max(dailychange))


# In[64]:


dailychange = [a for a in dailychange if a is not None]
dailychange.sort()
print('The smallest change in one day (based on High and Low price)',*dailychange[:1])


# ### What was the largest change between any two days (based on Closing Price)?

# In[65]:


close_index = json_data['dataset']['column_names'].index('Close')
close_index


# In[66]:


close_change =[]
for i in json_data['dataset']['data']:
    close = i[close_index]
    close_change.append(close)
#close_change


# In[67]:


close= [i-j for i,j in zip(close_change,close_change[1:])]
#close


# In[68]:


print('The largest change between any two days:', max(close))


# ### What was the average daily trading volume during this year?

# In[69]:


trade_index = json_data['dataset']['column_names'].index('Traded Volume')
trade_index


# In[70]:


tradevol = []

for i in json_data['dataset']['data']:
    vol = i[trade_index]
    tradevol.append(vol)


# In[71]:


def avg(lst): 
    return sum(lst)/len(lst)


# In[72]:


avg(tradevol)


# ### (Optional) What was the median trading volume during this year. (Note: you may need to implement your own function for calculating the median.)

# In[73]:


def median(lst): 
    sortlst = sorted(lst) 
    lstlen = len(lst)
    index = (lstlen - 1) // 2
    
    if (lstlen%2): 
        return sortlst[index]
    else: 
        return (sortlst[index] + sortlst[index + 1])/2.0


# In[74]:


median(tradevol)

