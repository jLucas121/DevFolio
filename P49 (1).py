# Program Name: 
# My Name: James Lucas Smith
# Program Number: P49
# Version: Python 3.1.6
# Date Started- Date Finished: 10/27/22-10/27/22
# Description:Pulls data from CSV file and shows AVG stock price per year

'''

Write a python program to calculate the average for each month of every year,
using the functions below:

# function name: get_data_list
# parameter:     FILE_NAME  - the file's name you saved for the stock's prices
# description:   reads a csv file, splits it by lines and puts it in a list
# returns:       a list of lines, each element on the list is a line in the csv file
def get_data_list (FILE_NAME):
    return data_list

# function name: get_monthly_averages
# parameter:     data_list  - the list that you will process
# description:   calculate monthly averages
# returns:       a list with sub-lists containing months, years, averages
def get_monthly_averages (data_list):
    return monthly_average_list # a list of lists [ [mm,yyyy,avg],..., [mm,yyyy,avg] ]

# function name: print_info
# parameter:     monthly_average_list  - the list that you will process
# description:   print the monthly averages of Google stock
# returns:       None
def print_info (monthly_average_list):
    # show monthly averages of Google stock

Calculate the averages for every month, store them in a list,
and then show the list to the user:

# call function to get the data list.
data_list = get_data_list(FILE_NAME)

# call to return a list with monthly averages
monthly_average_list = get_monthly_averages(data_list)

# call to show monthly_average_list as shown in the sample run below
print_info(monthly_average_list)

Save and submit it as p49.py

'''

#name: get_data_list
#param: FILE_NAME - the file's name you saved for the stock's prices
#description: reads a csv file, splits it by lines and puts it in a list
#return: a list of lines, each element on the list is a line in the csv file
def get_data_list(FILE_NAME):
#set up needed variables
    file_temp = open('table-1.csv', "r")#file name and 'r' to denote what action to take, IE "Read"
    list_major = []
    list_minor = []
    list_final = []
#take out \n
    for x in file_temp:
        hold = x.replace("\n", "")
        list_minor.append(hold)
    for x in list_minor:
        list_major.append(x.split(','))
#close file and return
    file_temp.close()
    return list_major

# function name: get_monthly_averages
# parameter:     data_list  - the list that you will process
# description:   calculate monthly averages
# returns:       a list with sub-lists containing months, years, averages
#return monthly_average_list # a list of lists [ [mm,yyyy,avg],..., [mm,yyyy,avg] ]
def get_monthly_averages(data_list):
    count=0
    total={}
    countDays={}
    average=[]
    for x in data_list:
        if count==0:
            count=count+1
            continue
        date=x[0].split('/');
        day=date[1]
        month=date[0]
        year=date[2]
        key=str(month)+"-"+str(year)
        if key in total.keys():
            total[key]=float(total[key])+float(x[6])
            countDays[key]=countDays[key]+1
        else:
            total[key]=x[6]
            countDays[key]=1
    count=0
    for k, v in total.items():
        averageValue=float(v)/int(countDays[k])
        average.append([k,averageValue])
        count=count+1
    return average

# function name: print_info
# parameter:     monthly_average_list  - the list that you will process
# description:   print the monthly averages of Google stock
# returns:       Lists of avg per year/month
# show monthly averages of Google stock    
def print_info(monthly_averages_list):
    count=1;
    print("monthly_averages_list[ 0] = ['Month', 'Year', 'Average']")
    for x in monthly_averages_list:
        month=x[0].split('-')[0]
        if int(month)<10:
            month='0'+str(month)
            year=x[0].split('-')[1]
        if(count<10):
            print("monthly_averages_list[ "+str(count)+"] = ['"+str(month)+"', '"+str(year)+"', '"+str(format(round(x[1],2)))+"']")
        else:
            print("monthly_averages_list["+str(count)+"] = ['"+str(month)+"', '"+str(year)+"', '"+str(format(round(x[1],2)))+"']")
        count=count+1

#calls functions
data_list = get_data_list("table-1.csv")
#calls data from .csv file
monthly_averages_list = get_monthly_averages(data_list)
#calls avg from list
print_info(monthly_averages_list)
#prints monthly avg
