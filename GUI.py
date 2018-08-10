# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:50:21 2018

@author: Miguel Petrarca
"""

import tkinter
import Extract_Data_and_Plot_Function
import Extract_Data_Function

#import Extract_Data_to_CSV



def exportCSV():
#    startTimeString= startEntry.get()
#    endTimeString= endEntry.get()
#    tags=(tagsEntry.get()).split(',')
#    filenames=(fileNamesEntry.get()).split(',')
#    
#    filtered_data=Extract_Data_Function.extract(startTimeString, endTimeString, tags, filenames)
#    filtered_data.to_CSV(path_or_buf='Extracted-Data.xlsx')
    return

def exportExcel():
    startTimeString= startEntry.get()
    endTimeString= endEntry.get()
    tags=(tagsEntry.get()).split(',')
    filenames=(fileNamesEntry.get()).split(',')
#    exported_filename= new_File_Name_Entry.get()
   

    
    filtered_data=Extract_Data_Function.extract(startTimeString, endTimeString, tags, filenames)
    filtered_data.to_excel(excel_writer='Exported-Data.xlsx')
    
    return

def generatePlot():
    
    startTimeString= startEntry.get()
    endTimeString= endEntry.get()
    tags=(tagsEntry.get()).split(',')
    filenames=(fileNamesEntry.get()).split(',')
    lineThickness=lineThicknessEntry.get()
    legendNaming=(legendNamingEntry.get()).split(',')
    

    Extract_Data_and_Plot_Function.plotData(startTimeString, endTimeString, tags, filenames, lineThickness, legendNaming)
    return


#Creating a blank window by calling constructor
root =tkinter.Tk()

#size of window
root.geometry("2000x1000")

#adding title to the window
root.title("Dr Fan's Lab Data Analysis Program")

#defining start label widget and start Entry widget
startLabel =tkinter.Label(root,text="Enter Starting Date and Time: ",font = "Helvetica 10 bold")
startEntry=tkinter.Entry(root, width=30)

#defining end label widget and start Entry widget
endLabel =tkinter.Label(root,text="Enter Ending Date and Time: ",font = "Helvetica 10 bold")
endEntry=tkinter.Entry(root, width=30)

#defining tags label widget and start Entry widget
tagsLabel=tkinter.Label(root,text="Enter tags separated by commas: ",font = "Helvetica 10 bold")
tagsEntry=tkinter.Entry(root, width=30)

#defining filename label widget and start Entry widget
fileNamesLabel =tkinter.Label(root,text="Enter Filenames of CSV file containing the data (If multiple files want to be used, separate by commas): ",font = "Helvetica 10 bold")
fileNamesEntry=tkinter.Entry(root, width=60)

#defining line thickness label widget and start Entry widget
lineThickness =tkinter.Label(root,text="Enter an integer representing the thickness of the lines on the graph: ",font = "Helvetica 10 bold")
lineThicknessEntry=tkinter.Entry(root, width=30)

#defining filename label widget and start Entry widget
legendNaming =tkinter.Label(root,text="Enter the name of each corresponding tag (this will be used as labels for the legend): ",font = "Helvetica 10 bold")
legendNamingEntry=tkinter.Entry(root, width=30)

##defining newly exported filename label widget and start Entry widget
#new_File_Name =tkinter.Label(root,text="If exporting, Please enter the name of the new file:  ",font = "Helvetica 10 bold")
#new_File_Name_Entry=tkinter.Entry(root, width=30)


startLabel.pack()
startEntry.pack()

endLabel.pack()
endEntry.pack()

tagsLabel.pack()
tagsEntry.pack()

fileNamesLabel.pack()
fileNamesEntry.pack()

lineThickness.pack()
lineThicknessEntry.pack()

legendNaming.pack()
legendNamingEntry.pack()

#new_File_Name.pack()
#new_File_Name_Entry.pack()






#Creating Button to Plot
plotButton= tkinter.Button(root,text="plot", font = "Helvetica 13 bold", command=generatePlot)

#Creating export button
exportCSVButton= tkinter.Button(root,text="Export data to a CSV",font = "Helvetica 13 bold", command=exportCSV)

#Creating export button
exportExcelButton= tkinter.Button(root,text="Export data to Excel",font = "Helvetica 13 bold", command=exportExcel)







#displays plot button in window
plotButton.pack()

#diplays export button in window
exportCSVButton.pack()

#diplays export button in window
exportExcelButton.pack()




#Constanty looping to display window unril window is closed
root.mainloop()



