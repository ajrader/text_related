
# coding: utf-8

# # to parse REDDIT COMMENTS FILE

# In[1]:

import os,sys


# In[2]:

from glob import glob
import pandas as pd
import numpy as np


# In[3]:

repodir = '/san-data/personal/kesj/public_data/reddit_comments_corpus/reddit_data/'
year = '2015/'
os.chdir(repodir)
os.chdir(year)
infile = glob('RC*')
infile


# In[ ]:

probe = pd.

