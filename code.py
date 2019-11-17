# --------------
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys
import csv

# Command to display all the columns of a numpy array
np.set_printoptions(threshold=sys.maxsize)
# Load the data. Data is already given to you in variable `path` 
sales_data=np.genfromtxt(path,delimiter=',',skip_header=1)
#print(data)
uadcam=np.unique(sales_data[:,1])
#print(uadcam)


# How many unique ad campaigns (xyz_campaign_id) does this data contain ? And for how many times was each campaign run ?
from collections import Counter
uadcam=np.unique(sales_data[:,1])
#print(uadcam)
# What are the age groups that were targeted through these ad campaigns?
age_groups = sales_data[:,3]
# What was the average, minimum and maximum amount spent on the ads?
min_amt = sales_data[:,8].astype(float).min()
max_amt = sales_data[:,8].astype(float).max()
avg_amt = sales_data[:,8].astype(float).mean()
# What is the id of the ad having the maximum number of clicks ?
max_clicks = sales_data[:,7].astype(float).max()
mask = (sales_data[:,7].astype(float) == max_clicks)
ad_id_maxclicks = sales_data[:,0][mask]
# How many people bought the product after seeing the ad with most clicks? Is that the maximum number of purchases in this dataset?
mask_1 = (sales_data[:,0] == ad_id_maxclicks)
pppls_bought = sales_data[:,-1][mask_1]
# So the ad with the most clicks didn't fetch the maximum number of purchases. Let's find the details of the product having maximum number of purchases
max_purchase = sales_data[:,-1].astype(int).max()
product_max_purchase = sales_data[sales_data[:,-1].astype(int) == max_purchase]
# Create a new feature `Click Through Rate`  (CTR) and then concatenate it to the original numpy array 
CTR = (sales_data[:,7].astype(int)*100)/sales_data[:,6].astype(int)
CTR = CTR.reshape(-1,1)
sales_data = np.concatenate((sales_data,CTR), axis=1)
# Create a new column that represents Cost Per Mille (CPM) 
CPM = (sales_data[:,8].astype(float)*1000)/sales_data[:,6].astype(int)
CPM = CPM.reshape(-1,1)
sales_data = np.concatenate((sales_data,CPM), axis=1)


