#!/usr/bin/env python
# coding: utf-8

# In[12]:


def Sentence(word1,word2):
    line = word1.replace(word2,'')
    return line.strip()
WORD ='     Python is very easy to understand, Python is easy to handle  '
x = Sentence(WORD,'Python')
print(x)


# In[ ]:




