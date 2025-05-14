# houses all methods for calculating statistics

# import preprocessing
import numpy as np

def calculate_highest_transaction_volume_or_value(df):
    index, highest_transaction_volume_or_value = np.where(df.values == df.values.max())
    highest_transaction_details = list(((df.index[index].values.tolist()[0] + 1),df.columns[highest_transaction_volume_or_value].values.tolist()[0]))
    return highest_transaction_details
    ...
    
# def calculate_highest_transaction_value():
#     ...

def calculate_lowest_transaction_volume_or_value(df):
    index, lowest_transaction_volume_or_value = np.where(df.values == df.values.min())
    lowest_transaction_details = list(((df.index[index].values.tolist()[0] + 1),df.columns[lowest_transaction_volume_or_value].values.tolist()[0]))
    return lowest_transaction_details

# def calculate_lowest_transaction_value():
#     ...

def calculate_average_transaction_volume_or_value(df):
    
    ...

def calculate_total_volume():
    ...

def calculate_total_value():
    ...
