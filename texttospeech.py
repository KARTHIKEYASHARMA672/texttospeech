#!/usr/bin/env python
# coding: utf-8

# In[3]:


# text to speech library
#Text to Speech Library 
# PYTTSx3
# install ptttsx3 
get_ipython().system('pip install pyttsx3')


# In[4]:


pip install --user --upgrade --force-reinstall pyttsx3


# In[5]:


import pyttsx3 as p
bot1= p.init()
voices=bot1.getProperty('voices')
bot1.setProperty('voice',voices[0].id)  # try another voice by changing voices[0] to voices[1]


# In[6]:


def text_to_speech(text):
    bot1.say(text)
    bot1.runAndWait()


# In[11]:


text_to_speech("Hi, Welcome to learn PYTHON PROGRAMMING FOR MODERN APPLICATION DEVELOPMENT ")
text_to_speech("ARE YOU ENJOYING THE SESSION.....                                                                    Good ")


# In[ ]:





# In[ ]:





# In[ ]:




