# open budget file
# get total number of months
# get net total amount of "Profit/Losses" over entire period
# change = current - previous
# average_change = sum all change/number of months changes
# greatest increase in profit: max(change) 
# greatest decrease in losses: min(change)
# open analysis file for writing the results
# print analysis results to terminal

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

increase_month = ""
decrease_month = ""

results = []

def average_change(numbers):
    length = len(numbers)
    total = 0
    for number in numbers:
        total += number
    return format((total / length), '.2f') 

def max_change(numbers):
    largest = 0

    for i in range(len(numbers)):
        if int(numbers[i]) > largest:
            largest = numbers[i]
    return largest

def min_change(numbers):
    smallest = 0

    for i in range(len(numbers)):
        if int(numbers[i]) < smallest:
            smallest = numbers[i]
    return smallest

# open file
# calculate monthly changes
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    
    previous_record = next(csvreader)
    ctr += 1
    net_total = int(previous_record[1])

    for row in csvreader:
        ctr += 1
        net_total += int(row[1])
        months.append(row[0])
        monthly_change = int(row[1]) - int(previous_record[1])
        changes.append(monthly_change)
        previous_record = row

# prepare analysis report
# calculate total net, total months, average change
header = "Financial Analysis"
separator = "-------------------------------"
total_months_line = f"Total Months: {ctr}"
total_net_line = f"Total: ${net_total}"
average_line = f"Average  Change: ${average_change(changes)}"

# calculate greatest increase in Profits/Losses
greatest_increase = max_change(changes)
change_index = changes.index(greatest_increase)
increase_month = months[change_index]
greatest_increase_line = f"Greatest Increase in Profits: {increase_month} (${greatest_increase})"

# calculate greatest decrease in Profits/Losses
greatest_decrease = min_change(changes)
change_index = changes.index(greatest_decrease)
decrease_month = months[change_index]
greatest_decrease_line = f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})"

results.append(header)
results.append(separator)
results.append(total_months_line)
results.append(total_net_line)
results.append(average_line)
results.append(greatest_increase_line)
results.append(greatest_decrease_line)

# write analysis to text file in Analysis folder
cleaned_file = zip(results)
output_file = os.path.join("Analysis", "output.txt")
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerows(cleaned_file)

# print analysis to terminal
for row in results:
    print(row)