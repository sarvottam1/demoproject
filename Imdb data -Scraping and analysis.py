#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing pythons library
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[2]:


# Sending http requests for getting data 
url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
# request for getting a page 
response= requests.get(url)


# In[3]:


soup = BeautifulSoup(response.content, 'html.parser')


# In[4]:


# creating an empty list, so we can add the value
movie_name =[]
year =[]
time=[]
rating=[]
metascore=[]
votes=[]
gross=[]
Stars=[]
Director=[]
genre=[]
description=[]


# In[5]:


#class were all necessary data is present
movie_data = soup.findAll('div', attrs = {'class':'lister-item-content'})


# In[6]:


for store in movie_data:
    name = store.h3.a.text
    movie_name.append(name)
    
    year_of_release = store.h3.find('span', class_ = 'lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
    year.append(year_of_release)
    
    runtime = store.p.find('span', class_ = 'runtime').text.replace(' min', '')
    time.append(runtime)
    
    rate = store.find('div', class_ = 'inline-block ratings-imdb-rating').text.replace('\n', '')
    rating.append(rate)
    
    meta  = store.find('span', class_ = 'metascore').text.replace(' ', '') if store.find('span', class_ = 'metascore') else '^^^^^^'
    metascore.append(meta)
    
    #getting gross and revenue
    value = store.find_all('span', attrs = {'name': 'nv'})
    
    vote = value[0].text
    votes.append(vote)
    #income
    grosses = value[1].text if len(value) >1 else '*****'
    gross.append(grosses)
    
    #movie_type
    movie_type = store.find('span',class_ = 'genre').text.replace('\n','')
    if len(movie_type)>1:
        genre.append(movie_type)
    else:
        genre.append('**')
    
    # Description of the Movies -- Not explained in the Video, But you will figure it out. 
    describe = store.find_all('p', class_ = 'text-muted')
    description_ = describe[1].text.replace('\n', '') if len(describe) >1 else '*****'
    description.append(description_)
    
    #Cast Details -- Scraping Director name and Stars -- Not explained in Video
    cast = store.find("p", class_ = '')
    cast = cast.text.replace('\n', '').split('|')
    cast = [x.strip() for x in cast]
    cast = [cast[i].replace(j, "") for i,j in enumerate(["Director:", "Stars:"])]
    Director.append(cast[0])
    Stars.append([x.strip() for x in cast[1].split(",")])

movie_DF = pd.DataFrame({'Name of Movie':movie_name, 'Release Year':year,'Duration':time,'IMDB-rating':rating,'Genre':genre,'About':description,'Vote':votes,'Income':gross,'Actors':Stars,'Director':Director})    
    
    
    
    


# 1 Display Top 10 rows of the Dataset

# In[7]:


movie_DF.head(10)


# In[8]:


movie_DF.info()


# In[9]:


movie_DF.tail(10)


# find the shape of data

# In[10]:


movie_DF.shape

Display the title of the movie whose Duration is more than 180minutes.
# In[11]:


movie_DF[movie_DF['Duration'].astype(int)>=180][['Duration','Name of Movie']]


# In[12]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


movie_DF.to_excel('movie.xlsx',index=False)


# In[14]:


#top 10 Highest rated movies title


# In[ ]:





# In[ ]:


top

