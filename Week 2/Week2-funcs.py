# This is an additional .py file that you can benefit
# You will see related citations of the functions given below, within the original WS script
# if they are really necessary to mention

# Necessary library list
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

### User defined function to find the upper and lower boundaries for the Tukey fences
def find_boundaries(array1D, fold):
    upper_quant = pd.Series(array1D).quantile(0.75)
    lower_quant = pd.Series(array1D).quantile(0.25)
    IQR = upper_quant - lower_quant
    lower_boundary = lower_quant - (IQR * fold) 
    upper_boundary = upper_quant + (IQR * fold)
    
    return upper_boundary, lower_boundary


