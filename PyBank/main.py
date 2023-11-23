import os
import csv

#creating a path to the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#initializing relevant variables
month_count = 0
total = 0
change_list = [] #saving the monthly change to a list to make it easier to find the average change
change = 0
last_month = 0
greatest_inc = 0
greatest_inc_month = ""
greatest_dec = 0
greatest_dec_month = ""

#reading in the csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #looping through each row (month) in the csv
    for month in csvreader:

        #making sure to ignore the header row month[0]
        if month[0] == "Date":
            month_count = month_count

        else:
        #totaling the month count
            month_count += 1
            total += int(month[1])

            if month_count > 1:
                #change can only be calculated when there's at least 2 data points
                change = int(month[1]) - last_month
                change_list.append(change)

                if month_count == 2:
                    #declaring that the first change value is the greatest increase and decrease
                    greatest_inc = change
                    greatest_inc_month = month[0]

                    greatest_dec = change
                    greatest_dec_month = month[0]

                else:
                    #seeing if subsequent monthly changes are the greatest increase 
                    #or decrease in profit and storing the greatest +/- changes
                    if change > greatest_inc:
                        greatest_inc = change
                        greatest_inc_month = month[0]
                    
                    if change < greatest_dec:
                        greatest_dec = change
                        greatest_dec_month = month[0]
            else:
                #when it is the first month of recorded data, there can be no change
                change = 0

            #storing current month as last_month after all necessary calculations/comparisons
            #so we can calculate the change for the next month. Casting to int is needed
            last_month = int(month[1])

#calculating average change outside of the loop so the change_list is complete
change_avg = round(sum(change_list)/len(change_list), 2) 

#printing outputs to terminal
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average Change: ${change_avg}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")

#writing outputs to a new text file PyBank.txt
with open("PyBank.txt", "w") as pybanktxt:
    pybanktxt.write("Financial Analysis\n")
    pybanktxt.write("----------------------------------------\n")
    pybanktxt.write(f"Total Months: {month_count}\n")
    pybanktxt.write(f"Total: ${total}\n")
    pybanktxt.write(f"Average Change: ${change_avg}\n")
    pybanktxt.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n")
    pybanktxt.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})")