
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



# In[40]:

wiki_data = pd.read_csv("stuff.csv", sep=', ', delimiter=',', header='infer', names=None)
politifact_data = pd.read_csv("politifact.csv", sep=', ', delimiter=',', header='infer', names=None)
# In[ ]:

thedata = pd.concat([wiki_data, politifact_data])

x = thedata['text']
y = thedata['truthVals']

x = x.astype(str)
y = y.astype(float)

# In[42]:

x = x.iloc[:].values
y = y.iloc[:].values


# In[43]:

#print y

print x[1]
print x[2]


# In[44]:

tk = keras.preprocessing.text.Tokenizer(num_words=2000, lower=True, split=" ")

tk.fit_on_texts(x)

x = tk.texts_to_sequences(x)


# In[45]:

max_len = 80
print "max_len ", max_len
print('Pad sequences (samples x time)')

x = sequence.pad_sequences(x, maxlen=max_len)



# In[49]:

print x
print y

# In[56]:

max_features = 50000
model = Sequential()
print('Build model...')

model = Sequential()
model.add(Embedding(max_features, 128, input_length=max_len))
model.add(LSTM(128))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(10))
model.add(Activation('softmax'))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='rmsprop',metrics=['accuracy'])


# In[60]:

model.fit(x, y=y, batch_size=200, epochs=5, verbose=1, validation_split=0.2, shuffle=True)



# In[ ]:



