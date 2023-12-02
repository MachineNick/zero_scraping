#!/usr/bin/env python
# coding: utf-8

# In[99]:


import requests

from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the website to scrape
url = "https://zorox.to/trending"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
soup.prettify

Name = []
Episode = []


n=soup.find_all(class_='d-title')
for i in n :
    Name.append(i.text)
   


epi =soup.find_all(class_='tick-item tick-eps')
for j in epi:
        Episode.append(j.text)
Trending_series = []
Trending_series.append([Name,Episode])
df= pd.DataFrame(Trending_series,columns=['Name','Episode'])
time.sleep(1)
df.to_csv('Trending_series',index=False)


# In[ ]:





# In[ ]:





# In[ ]:




