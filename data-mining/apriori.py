import os
import pandas as pd
import sys
from scipy.io import arff
from collections import OrderedDict
import itertools
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import time


DATA = 'vote.arff'

data = arff.loadarff(DATA)
df = pd.DataFrame(data[0])

# Decode the data from its binary representation
# To a string representation
for column in df:
    df[column] = df[column].str.decode(encoding='utf-8')

# Get dummies to help with math
# in the C k tables
df = pd.get_dummies(df)

# Cast the whole data set to int type
# so that we can do math with it
for column in df:
    df[column] = df[column].astype(int)



def main(data, min_conf, min_support):
    headers = list(data)
    # C_k table place holder to be a list of headers
    # from our database
    c_k =  list(map(lambda i: [headers[i]], range(len(headers))))

    # Create the frequent itemset container to
    # store the result at each iteration of 
    # the pruning process
    L = []

    l_k = generate_frequent_itemset

    return data

main(df, .55, .55)