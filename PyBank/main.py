# open file
# get total number of months
# get net total amount of "Profit/Losses" over entire period
# change = current - previous
# average_change = sum all change/number of changes
# greatest increase in profit: max(change) where change > 0
# greatest decrease in losses: min(change) where change < 0
# print analysis results to terminal
# open a file for writing the results

import os
import csv

# path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

#lists to store profit/loss changes
months = []
changes = []
ctr = 0
monthly_change = 0

# open file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    previous_record = next(csvreader)
    ctr += 1
    print(f"first record  {previous_record}")

    for row in csvreader:
        ctr += 1
        months.append(row[0])
        monthly_change = int(row[1]) - int(previous_record[1])
        changes.append(monthly_change)
        previous_record = row

        #print(row)
        #print(row[0] + " " + str(row[1]))

print(str(ctr)) #total number of months included in the data set
print(changes[0])
print(months[0])

