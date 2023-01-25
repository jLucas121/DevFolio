# Program Name: Avg Sunspots
# My Name: James Lucas Smith
# Program Number: P48
# Version: Python 3.1.6
# Date Started- Date Finished: 10/21/22-10/21/22
# Description:Reads sunspots file, then inputs avg for data in sunspots and deposits avg in new file

'''
..and computes the average for each year,
writing them one per line to a file averages.txt (as shown below):

# Open the File to Read
myFile = open('sunspots.txt', 'r')
# Read the data from file into a list
listOfLines = myFile.read().splitlines() 
# Each list item is a new line from the file
listItem = listOfLines[0].split() # split each line by spaces
print(listItem) # shows list of strings ['1945','18.5','11.8',...,'28.4']
# Convert each of the strings to float in order to do math with them!


'''

#opens file sunspots.txt 
myFile = open('sunspots.txt', 'r')#opens and only reads file
listofSunSpots = myFile.read().splitlines()
myFile.close()#splits file into lines
for i in range(0,64,1):#runs through all 64 years and turns each into line
    listItem = listofSunSpots[i].splitlines()#splits data
##    print(listItem)#shows lists
newnewFile = open('averages.txt','w')#creates new file averages.txt
newnewFile.write('year ==== average \n')##header
for j in range(0,len(listofSunSpots),1):#iterates through whole list
    oneLine = listofSunSpots[j]
    oneLineData = oneLine.split()
    year = oneLineData[0]#year will always be first index in line
    sumData = 0#set count to 0
    for i in range(1,len(oneLineData),1):
        sumData += float(oneLineData[i])#convert to float since data is not whole
    avg = sumData/(len(oneLineData)-1)#computes avg for line, -1 so it doesnt account for year in avg
    newnewFile.write('%s      %.2f \n' %(year , avg))#writes year and avg per line
newnewFile.close()#close file so it saves

'''
Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

=============================== RESTART: /Users/lucas/Desktop/P48.py ===============================

=============================== RESTART: /Users/lucas/Desktop/P48.py ===============================

'''

