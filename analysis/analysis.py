import numpy as np
from features import feature_extraction

dataObj = feature_extraction()
train, validation, test = dataObj.process_text(dataObj.data)
# calculate the most common words in data set
dataObj.calc_common_words(dataObj.data)  # will output a text file
