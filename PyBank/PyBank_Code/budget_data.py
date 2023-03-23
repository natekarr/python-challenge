import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

#Variables needed beforehand
total_months = 0
total_profit = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""
lastMonth = 0
total_change = 0
firstRow = 1
#Loop through budget data
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #Skip header
    next(csvreader)
    for row in csvreader:
        #If the firstrow, now change occurs
        if firstRow == 1:
            change = 0
            firstRow = 0
        else:
            #Calculate change as curent month profit - previous month profit
            change = int(row[1]) - lastMonth
        #Add change to overall total and set this month to last month, increase month count and add profit to total profit
        total_change += change
        lastMonth = int(row[1]) 
        total_months += 1
        total_profit += int(row[1])
        #See if current amount of change is greater than previous greatest increase or less than previous greatest decrease
        if change > 0:
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = str(row[0])
        else:
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = str(row[0])
#Calculate the average amount of change over the period, subtract total months by 1 because the first month had no change
average_change = round(total_change / (total_months - 1), 2)

#Output to file and terminal
with open('../Analysis/budget_data_output.txt', 'w') as f:
    print("Finacial Analysis")
    f.write("Finacial Analysis\n")
    print("--------------------------------")
    f.write("--------------------------------\n")
    print(f"Total Months: {total_months}")
    f.write(f"Total Months: {total_months}\n")
    print(f"Total: ${total_profit}")
    f.write(f"Total: ${total_profit}\n")
    print(f"Average Change: ${average_change}")
    f.write(f"Average Change: ${average_change}\n")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    f.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")