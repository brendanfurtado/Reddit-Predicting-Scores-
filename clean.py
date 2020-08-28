from data_loading import *

data = data_loading.dataframe

# checking for null values, there are none
(data.isnull().values.any())

print(data.controversiality.value_counts())

# Cleaning part
