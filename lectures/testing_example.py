
# coding: utf-8

# In[23]:


import unittest


# In[28]:


BOOM


# In[44]:


class TestCase(unittest.TestCase):
    def test_pass(self):
        assert True
        
    def test_fail(self):
        assert False
        
    def test_error(self):
        x, y = 1, 0
        x/y


# In[45]:


unittest.main(argv=['foo'], exit=False, verbosity=2);


# In[46]:


import pytest


# In[ ]:


get_ipython().system('jupyter nbconvert --to script --output testing_example TestingExample.ipynb')
pytest.main(['-l', 'testing_example.py'])


# In[42]:


get_ipython().system('pytest -l testing_example.py')

