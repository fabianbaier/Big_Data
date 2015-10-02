# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 10:01:21 2015

@author: fabianbaier
"""

//r programming corsera quiz 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# where am I?
pwd
# change to my working directory
cd /Users/fabianbaier/Documents/Takshila/2015/Big Data/class3_092715


hw1 = pd.read_csv('hw1_data.csv')

hw1.isnull().sum()

hw1.Ozone.dropna().mean()

hw1[((hw1.Ozone) > 31) & ((hw1.Temp) > 90)]['Solar.R'].mean()

hw1[((hw1.Month) == 6)]['Temp'].mean()

(hw1.Month == 5)['Temp']

hw1[(hw1.Month == 6)].describe()

