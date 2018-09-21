import numpy as np
import pandas as pd 
pd.set_option('display.max_columns', 500)


dtrain = pd.read_csv("dataset/train.csv")
dtest  = pd.read_csv("dataset/test.csv")
print(dtrain[:10])

print(dtrain.describe())

# print("Hello world")