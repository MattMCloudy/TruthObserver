
# coding: utf-8

# In[38]:

from __future__ import absolute_import
from __future__ import division
import keras
import keras.preprocessing.text

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM

import string
import sys
import numpy as np
import pandas as pd
from six.moves import range
from six.moves import zip
import warnings


# In[39]:

get_ipython().system(u'ls')
get_ipython().system(u'cd TruthObserver/')
get_ipython().system(u'ls')


# In[40]:

thedata = pd.read_csv("stuff.csv", sep=', ', delimiter=',', header='infer', names=None)


# In[ ]:


x = thedata['text']
y = thedata['truthVals']


# In[42]:

x = x.iloc[:].values
y = y.iloc[:].values


# In[43]:

#print y

print x[1]
print x[2]


# In[44]:

tk = keras.preprocessing.text.Tokenizer(num_words=2000,  lower=True, split=" ")

tk.fit_on_texts(x)

x = tk.texts_to_sequences(x)


# In[45]:

max_len = 80
print "max_len ", max_len
print('Pad sequences (samples x time)')

x = sequence.pad_sequences(x, maxlen=max_len)



# In[49]:

print x[4]


# In[56]:

max_features = 20000
model = Sequential()
print('Build model...')

model = Sequential()
model.add(Embedding(max_features, 128, input_length=max_len, dropout=0.2))
model.add(LSTM(128, dropout_W=0.2, dropout_U=0.2))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop',metrics=['accuracy'])


# In[60]:

model.fit(x, y=y, batch_size=200, nb_epoch=1, verbose=1, validation_split=0.2, shuffle=True)



# In[ ]:



