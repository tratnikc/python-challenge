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
change_ctr = 0
net_total = 0
monthly_change = 0

greatest_increase = 0
greatest_decrease = 0

def average_change(numbers):
    length = len(numbers)
    total = 0
    for number in numbers:
        total += number
    return total / length 

def max_change(numbers):
    largest = 0

    for i in range(len(numbers)):
        if int(numbers[i]) > largest:
            largest = numbers[i]
    return largest

# open file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    previous_record = next(csvreader)
    ctr += 1
    net_total = int(previous_record[1])
    print(f"first record  {previous_record}")
    #print(str(net_total))

    for row in csvreader:
        ctr += 1
        net_total += int(row[1])
        months.append(row[0])
        monthly_change = int(row[1]) - int(previous_record[1])
        changes.append(monthly_change)
        previous_record = row
        print(f"previous record  {previous_record}")

        
        change_ctr += 1

        #print(row)
        #print(row[0] + " " + str(row[1]))

print(f"length of changes list {len(changes)}")
print(f"total number of months included in the data set {ctr}") #total number of months included in the data set
print("net total " + str(net_total)) #net total amount of "Profit/Losses"

print(f"average = {average_change(changes)}") # average change

print(f"largest {max_change(changes)}")
 
cleaned_file = zip(months,changes)
output_file = os.path.join("output.csv")
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerows(cleaned_file)

        # print(f"{changes[x]}")


#print(months)
#print(f"{months} {str(monthly_change)} ")
