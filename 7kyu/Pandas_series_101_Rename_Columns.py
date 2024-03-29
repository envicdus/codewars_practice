'''
Input parameters
pandas.DataFrame object
sequence
Task
Your function must return a new pandas.DataFrame object with same data than the original input 
but now its column names are the elements of the sequence. You must not modify the original input.

The number of columns of the input will always be equal to the size of the sequence.

Examples
   0  1  2
0  1  2  3
1  4  5  6

names = ['A', 'B', 'C']
   A  B  C
0  1  2  3
1  4  5  6
'''

# my solution

import pandas as pd

def rename_columns(df, names):  
    # your code here
    title = list(names)
    df=pd.DataFrame(df, copy=True)
    df.columns = title
    return df

# other solution

# 1
import pandas as pd

def rename_columns(df, names):  
    return pd.DataFrame(data=df.values, columns=names)

# 2

import pandas as pd

def rename_columns(df, names):  
    df2 = df.copy()
    df2.columns = names
    return df2

# 3

import pandas as pd

def rename_columns(df, names):  
    return df.rename(
        columns=dict(zip(df.columns, names)))