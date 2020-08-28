import numpy as np
from features import feature_extraction

dataObj = feature_extraction()
train, validation, test = dataObj.process_text(dataObj.data)
