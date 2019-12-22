#
#  Udacity - Machine Learning Engineer Nanodegree
#  Capstone Project - Saudi Stock Prediction 
#  Ageel Assif
#  12/4/2016
#  This script aims to combine all the data CSV files into one master sheet with all the data


import glob
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

# The Output will be a file called combined.csv
combined_file = 'combined.csv'
start_date = '01/01/2009'
end_date =  '11/28/2019'
#Check if a combined file exist and delete if it dose
if os.path.exists(combined_file):
  os.remove(combined_file)
  print('Old file deleted')

#Read the base CSV , in our case TASI. We only need the Date and Price columns
tasi_df = pd.read_csv('TASI.csv', thousands=',', decimal='.')
tasi_df = tasi_df[['Date','Price']]

#Our inital Dataframe is just the TASI data, we loop over all the files in the folder 
# (except TASI) and combine the data based on the Date column.
# Note that the merge process will match the dates across all our files and we will lose dates that dont match up
combined_df = tasi_df
for f in glob.glob('*.csv'):     
     if f != 'TASI.csv':

        df = pd.read_csv(f, thousands=',', decimal='.')
        #df.interpolate(method='linear', limit_direction='forward', axis=1 )

        df['Price'] = df['Price'].interpolate()
        if 'Open' in df:
                df['Open'] = df['Open'].interpolate()
        if 'Low' in df:
                df['Low'] = df['Low'].interpolate()
        if 'High' in df:
                df['High'] = df['High'].interpolate()
# We assign a prefix to the new columns to be able to identify the data source        
        prefix = (f.split('.'))[0]+'_'
        df = df.add_prefix(prefix)
        print('Trying to merge '+f+' '+str(df.shape))
#       When using merge method , we only retain the records with data for the same date accross all datesets
#       Therefore we drop a lot of records. We only get about 720 out of 3507.
#       Therefore I have switched to concat to retain all the dates for TASI and matching if avaible from others        
#        combined_df = pd.merge(combined_df,df, left_on=['Date'],right_on=[prefix+'Date'])        
        combined_df = pd.concat([combined_df, df], axis=1).reindex(combined_df.index)

#Convert Volume from string to numbers (i.e 5.2M to 5200000)
#https://stackoverflow.com/questions/5459256/python-parse-a-string-with-custom-price-units
        def numerize(s):               
                try:
                        if str(s) == 'nan':
                                return 0
                        elif str(s) == '-':
                                return 0                       
                        multipliers = {'K': 10**3, 'M': 10**6, 'B': 10**9}                      
                        if s[-1] in multipliers:
                                return float(s[:-1]) * multipliers[s[-1]]
                        else:
                                return float(s)
                except TypeError:
                        return s

        if(prefix+'Vol.' in combined_df):               
                combined_df[prefix+'Vol.']  = combined_df[prefix+'Vol.'].apply(numerize)                 
                combined_df[prefix+'Vol.']  = combined_df[prefix+'Vol.'].interpolate(method='nearest')



# Remove extra Date columns :
# Remove Duplicate Date column 
# Percent Change will be dropped as its a cacluated field from existing columns
# Columns Close , Low , High will be anlayzed and keept if they pose any affect     
#combined_df = combined_df[combined_df.columns.drop(list(combined_df.filter(regex='_Date|Change|Low|High')))]     
combined_df = combined_df[combined_df.columns.drop(list(combined_df.filter(regex='_Date|Change|Adj|Low|High|Close|Open')))]     



#Convert from String to Date to pick the date range 2009 - 2019
combined_df['Date'] = pd.to_datetime(combined_df['Date'])
combined_df = combined_df[combined_df.Date.between(start_date, end_date)]

# Save file
combined_df.to_csv(combined_file, encoding='utf-8', index=False)
print('Generated '+combined_file+' which contains '+str(combined_df.shape[0])+' rows and '+str(combined_df.shape[1])+' Columns')


#Data Processing notes
# Date columns had to be unified in format & Unified names 'Vol.' 'Volume'
# The Files have to be reviewed to ensure they have the same date range , otherwise our data set would shrink
# i.e ALAHLY.CSV only had data from 2014 which reduced out end dataset and I had to replace it
# Interpolate the null values
