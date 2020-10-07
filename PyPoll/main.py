#open election data file
#get total number of votes cast
#list of candidates who received votes

import os
import csv

election_results = []
total_votes = 0

# path to collect data from Resources folder
votes_csv = os.path.join("Resources", "election_data.csv")

#check for duplicate votes
with open(votes_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
        election_results.append(row[2])

total_votes = len(election_results)
khan_votes = election_results.count("Khan")
correy_votes = election_results.count("Correy")
li_votes = election_results.count("Li")
otooley_votes = election_results.count("O'Tooley")

print(f"Total Votes: {total_votes}")
print(f"Khan: {khan_votes}")
print(f"Correy: {correy_votes}")
print(f"Li: {li_votes}")
print(f"O'Tooley: {otooley_votes}")
    


