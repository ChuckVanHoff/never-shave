<b> The motivation </b>

Many people choose a colege path after high school becuase of the promises for higher wages, more longterm security, and a generally higher standard of living living. We analyzed a plethora of data ranging from individual demographics to pre-college preparations to see how much truth there is to those claims, to root out any reliable predictors to help better guide one through their college choices, and to find out if it's all really worth it. Here is what we found.....

<b> The Data </b>

The data for this project came from <a href="playingwithfyre.html">https://collegescorecard.ed.gov/data/</a>, and was cleaned and organized using Jupyter Notebooks. Separte data files were gleaned out of the full dataset for each of the three models generated from SciKit Learn techniques for machine learning.

<b> The Process </b>

After cleaning the data we used the SciKit Learn library to create three predicitve models: 
  College type - public, private for profit, private not for profit
  Earnings after ten years - based on the college's minimum SAT requirements
  Earnings after ten years - based on the earnings 6th, 7th, and 8th years earnings

Models were create using logistics regression for college type, K neighbors for earning from SAT, and linear regression for earnings from previous earnings.

<b> The results </b>

