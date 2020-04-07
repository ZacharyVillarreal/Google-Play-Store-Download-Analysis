#!/usr/bin/env python
# coding: utf-8

# # Imports

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from datetime import datetime, date
from string import *


#Data Cleaning


def remove_non_num_str_rows(df, col):
    '''
    remove_non_num_str_rows: takes in a Pandas DataFrame, DataFrame column
    and removes the rows with strings containing non-numerical strings

    Parameters
    ----------
    df: Pandas Dataframe
    col: Pandas column (df.column_name)

    Returns
    -------
    DataFrame with dropped rows
    '''
    accum_row_idx_list = []
    drop_list = []
    for _ in col:
        for j in _:
            if j in ascii_letters:
                accum_row_idx_list.append(df.index[col == _].tolist())
    for _ in accum_row_idx_list:
        for j in _:
            drop_list.append(j)
    df.drop(drop_list, axis = 0, inplace = True)


def remove_spaces(string): 
    '''
    remove_spaces: takes in a string and removes spaces
    
    Parameter
    ---------
    string: python string
    
    Returns
    -------
        Python string with no spaces
    '''
    return string.replace(" ", "") 


def convertible_to_float(string):
    '''
    convertible_to_float: takes in a string and determines if the string is able to convert to a float
    if not, and occurs ValueError, returns False

    Parameter
    ---------
    string: Python string

    Returns
    -------
    True/False on the basis of string to float conversion
    '''
    try:
        float(string)
        return True
    except ValueError:
        return False

    
def replace_non_date_str_rows(df, col):
    '''
    remove_non_num_str_rows: takes in a Pandas DataFrame, DataFrame column
    and removes the rows with strings containing non-numerical strings

    Parameters
    ----------
    df: Pandas Dataframe
    col: Pandas column (df.column_name)

    Returns
    -------
    DataFrame with rows equalling NaN values
    '''
    drop_list = []
    for _ in col:
        if _[0] not in ascii_letters:
            drop_list.append(_)
    col = col.replace(drop_list, np.nan)


def replace_non_size_str_rows(col):
    '''
    remove_non_size_str_rows: takes in a Pandas DataFrame column, 
    replacingthe rows that contain non-numerical values with NaN

    Parameters
    ----------
    col: Pandas column (df.column_name)

    Returns
    -------
    DataFrame with rows equalling NaN values
    '''
    for _ in col:
        for j in _:
            if j not in '.1234567890':
                col = col.replace(_, np.nan)

                
#EDA


def normalize_col(df, col):
    df[col] = (
        df[col]-df[col].min())/(df[col].max()-df[col].min())

