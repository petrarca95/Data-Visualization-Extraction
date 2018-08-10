# -*- coding: utf-8 -*-
"""
Created on Wed May 16 22:16:44 2018

@author: Miguel Petrarca
"""

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt




    # Prompt user for start date/time and end date+time
        
#print('use following format for date and time: month/day/year hour:minute:second')
#startTimeString=input('Enter the starting time:')
#endTimeString = input ('Enter the ending time: ' )


#Populate list of tags with tag names. This will be used to extract tags from DataFrame
#tags = input("Enter the tags you want to extract each separated by a comma: " ).split(',')
#filenames = input("Enter filenames separated by commas: ").split(',')



def plotData(startTimeString, endTimeString, tags, filenames, lineThickness, legendNaming):

    #Convert input (which is in a string format) to a datetime object (in order to be able to use operators)
    dateTimeStart = datetime.strptime(startTimeString, '%m/%d/%Y %H:%M:%S')
    dateTimeEnd = datetime.strptime(endTimeString, '%m/%d/%Y %H:%M:%S')
    
    
    
    
    
    #Index j only will be used to label legend
    j=1
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
        
        
        #%%
        #Index variable k is used to label the legend with the desired name inputed by the user
        #(legendNaming variable) comes from the GUI input
        k=0
        
        #Plotting each user specified tag vs datetime for all specifed tags
        for individualTag in tags:
            plt.plot(dateTimes,dfFinal[individualTag], label=legendNaming[k]  + " From File " + str(j), linewidth=lineThickness)
            k=k+1

            
        plt.legend(fontsize=20, loc ='best')
        plt.xlabel('Day-Month-Hour (from 0 to 24 hours)',fontsize=35, labelpad=70)
        plt.xticks(fontsize='30')
        plt.yticks(fontsize='30')
        
        
        plt.grid(True)
        j=j+1
    
    return





    

    
    
    

    
    
    


