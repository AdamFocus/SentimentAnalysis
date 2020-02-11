#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np

data = pd.read_csv('ChnSentiCorp_htl_all.csv', names=['label', 'text'])

# shuffle
data_index = np.random.permutation(np.arange(len(data)))
train_index = data_index[:int(0.7*len(data_index))]
test_index = data_index[int(0.7*len(data_index)):]

# reset index
train = data.iloc[train_index, :].reset_index(drop=True)
test = data.iloc[test_index, :].reset_index(drop=True)

# save
train.to_csv('train.csv', index=True, sep='\t')
test.to_csv('test.csv', index=True, sep='\t')

