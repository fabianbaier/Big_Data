Install on your Mac Anaconda distribution with Python 2.7
https://www.continuum.io/downloads
Follow the installation instructions for Python 2.7 for your computer (e.g. “Mac Install). Note: There is a Python 3, which has significant differences from 2.7 and is not “industry standard.” We will be using Python 2.7. 

Mac only: Test that Anaconda and Python were installed correctly by opening a Terminal window and entering ipython notebook In a few moments, your browser should open to a window titled Jupyter. If this works, you may close your browser, return to the terminal window, and shutdown the notebook server.  

Install Spyder or Rodeo 
pip install spyder
or
pip install rodeo

then simply launch through the terminal
spyder
																									

##what are the column names of the dataset?																									
Ozone	Solar.R	Wind	Temp	Month	Day																				
																									
#Extract the first 2 rows of the data frame and print them to the console. What does the output look like?																									
Ozone	Solar.R	Wind	Temp	Month	Day																				
41	190	7.4	67	5	1																				
36	118	8	72	5	2																				
																									
#How many observations (i.e. rows) are in this data frame?																									
153																									
																									
#Extract the last 2 rows of the data frame and print them to the console. What does the output look like?																									
Ozone	Solar.R	Wind	Temp	Month	Day																				
18	131	8	76	9	29																				
20	223	11.5	68	9	30																				
																									
#What is the value of Ozone in the 47th row?																									
NA																									
																									
#How many missing values are in the Ozone column of this data frame?																									
37																									
																									
#What is the mean of the Ozone column in this dataset? Exclude missing values (coded as NA) from this calculation.																									
42.12931034																									
																									
#Extract the subset of rows of the data frame where Ozone values are above 31 and Temp values are above 90. What is the mean of Solar.R in this subset?																									
212.8																									
																									
#What is the mean of "Temp" when "Month" is equal to 6? 																									
79.1																									
																									
#What was the maximum ozone value in the month of May (i.e. Month = 5)?																									
71																									
