
# coding: utf-8

# # to parse REDDIT COMMENTS FILE

# In[2]:

import os,sys


# In[3]:

from glob import glob
import pandas as pd
import numpy as np


# In[4]:

repodir = '/san-data/personal/kesj/public_data/reddit_comments_corpus/reddit_data/'
year = '2015/'
os.chdir(repodir)
os.chdir(year)
infile = glob('RC*')
print infile[0]
sample = glob('*.json')
print sample[0]


# In[18]:

with open(infile[0]) as rc_file:
    row1 = rc_file.readline().strip()
    print row1
    row2 = rc_file.readline().strip()
    print row2


# In[11]:

with open(sample[0]) as json_file:
    sample_data = json_file.readlines()
    
sample_data = [a.split('\n') for a in sample_data] 
print len(sample_data)


# In[18]:

sample_data[0][0]


# In[5]:

probe = pd.read_json(sample[0])


# In[10]:

pd.__version__


# In[ ]:

probe = pd.read_json(infile[0])


# In[9]:

import json
fromprint import pprint

with open(infile) as data_file:    
    data = json.load(data_file)

pprint(data)


# In[ ]:




# In[8]:

with open(infile)


# In[ ]:

probe = pd.read_json


# In[7]:

pd.read_json(infile


# In[ ]:



