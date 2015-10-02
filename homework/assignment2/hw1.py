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

##what are the column names of the dataset?
hw1.describe()

#Extract the first 2 rows of the data frame and print them to the console. What does the output look like?
hw1.head(2)

#How many observations (i.e. rows) are in this data frame?	
hw1.shape[0]

#Extract the last 2 rows of the data frame and print them to the console. What does the output look like?	
hw1.sort(ascending=False).head(2)

#What is the value of Ozone in the 47th row?
hw1.Ozone[47]

#How many missing values are in the Ozone column of this data frame?	
hw1.isnull().sum()

#What is the mean of the Ozone column in this dataset? Exclude missing values (coded as NA) from this calculation.
hw1.Ozone.dropna().mean()

#Extract the subset of rows of the data frame where Ozone values are above 31 and Temp values are above 90. What is the mean of Solar.R in this subset?
hw1[((hw1.Ozone) > 31) & ((hw1.Temp) > 90)]['Solar.R'].mean()

#What is the mean of "Temp" when "Month" is equal to 6? 
hw1[((hw1.Month) == 6)]['Temp'].mean()

#What was the maximum ozone value in the month of May (i.e. Month = 5)?
(hw1.Month == 5)['Temp']

hw1[(hw1.Month == 6)].describe()

