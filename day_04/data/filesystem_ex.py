#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("Welcome to Jupyter")


# Here in this notebook we will experiment on OS and other important python modules for controlling the file system and directory structure

# In[4]:


import os
import os.path
import shutil
import subprocess


# In[6]:


os.getcwd()


# Organizer Logic

# In[7]:


root = r"C:\Users\Purushotham\Desktop\oracle\day_04\data"
os.chdir(root)
os.getcwd()


# Get all the extensions

# In[9]:


files = os.listdir()
files


# In[14]:


os.path.splitext("data.ext")[1][1:]


# In[15]:


exts = []
for file in files:
    exts.append(os.path.splitext(file)[1][1:])
exts


# In[16]:


for ext in set(exts):
    os.mkdir(ext)


# Move the files one by one

# In[19]:


for file in files:
    src = file
    ext = os.path.splitext(file)[1][1:]
    dest = os.path.join(root, ext)
    shutil.move(src, dest)

