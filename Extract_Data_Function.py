# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 19:25:37 2018

@author: petra
"""

import pandas as pd
from datetime import datetime



#Convert input (which is in a string format) to a datetime object (in order to be able to use operators)


def extract(startTimeString, endTimeString, tags, filenames):
    #Convert input (which is in a string format) to a datetime object (in order to be able to use operators)
    dateTimeStart = datetime.strptime(startTimeString, '%m/%d/%Y %H:%M:%S')
    dateTimeEnd = datetime.strptime(endTimeString, '%m/%d/%Y %H:%M:%S')
    
    
    
    
    
    #Index j only will be used to label legend
    for name_of_file in filenames:
        # Loading csv file with data into DataFrame object
        dfCSV = pd.read_csv(name_of_file.strip(' '))
        
        
        
        #%%
        
        # Concatenate date and time columns, both of type str, into a single string. Space in between the two is added for formatting
        dfCSV['Time'] = dfCSV['Date'] + ' ' + dfCSV['Time']
        
        
        #%%
        #Replacing time column with the date time object version of the corresponding strings (actually the function changes strings to Timestamp objects)
        #this is done in order to be able to use logical operators and 
        dfCSV['Time'] = pd.to_datetime(dfCSV['Time'], format = '%m/%d/%Y %H:%M:%S')
        #%%
        
        
        #We extract only the relevant time interval and store it in another DataFrame. Subset of dfCSV DataFrame
        #True for rows we want to extract False for rows outside specifed time range
        dfCorrectTimeInterval = (dfCSV['Time']<=dateTimeEnd) & (dfCSV['Time']>=dateTimeStart)
        
        #%%
        
        #Create an empty DataFrame object by specfying the number of indexes needed, and the columns name will be populated by the list of tags.
        #DataFrame filled with boolean values, True for the rows we want to extract
        dfFinal = pd.DataFrame(index=range(0,dfCorrectTimeInterval.shape[0]),columns=tags)
        
        
        #%%    
        #Using the boolean DataFrame, which contains True for the specified time interval, to extract timeStamp values we want to graph
        dateTimes= dfCSV[dfCorrectTimeInterval]['Time']
            
        
        #%%
        #for loop to populate new DataFrame which is a subset of dfCorrectInterval and only contains tags of interest
        for tagValue in tags:
            dfFinal[tagValue] = dfCSV[tagValue]
            
        
        #%%
            
        #Extracting only the time span we are interested in by using the dataframe filled with boolean values (True=Within our time range)
        dfFinal=dfFinal[dfCorrectTimeInterval]
        
        return dfFinal
    
#dff=extract('07/15/2018 0:0:0','07/16/2018 2:0:0',['FC211_CV','FT320'],['20180715150757.csv','20180716000000.csv'])
#dff.to_excel(excel_writer='Extracted-Data.xlsx')
