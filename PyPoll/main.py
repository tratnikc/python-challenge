# open election data file
# get total number of votes cast
# list of candidates who received votes
# get total number of votes and percentages each candidate received
# list the winner of the election based on popular vote

import os
import csv

election_results = []
candidates = []
tally_results = []
poll_results = []
total_votes = 0

def percentage_vote(counts):
    pct = 0
    pct = (counts / total_votes) * 100
    return format(pct, '.3f') + '%'

def tally_votes():
    vote_count = 0
    vote_pct = 0
    for running_man in candidates:
        vote_count = election_results.count(running_man)
        vote_pct = percentage_vote(vote_count)
        tally_results.append((running_man, vote_pct, vote_count))

# path to collect data from Resources folder
votes_csv = os.path.join("Resources", "election_data.csv")

with open(votes_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
        election_results.append(row[2])

#list of candidate names
candidates = set(election_results)

#total number of votes cast
total_votes = len(election_results)

#names of candidates
#total number of votes each candidate won
#percentage of votes each candidate won
tally_votes()

#sort to get the candidate with the most number of votes
sorted_results = sorted(tally_results, key=lambda item:item[2], reverse=True)

# prepare analysis report
header = "Election Results"
separator = "--------------------------"
total_line = f"Total Votes: {total_votes}"
winner_line = f"Winner: {sorted_results[0][0]}"

poll_results.append(header)
poll_results.append(separator)
poll_results.append(total_line)
poll_results.append(separator)

for line in sorted_results:
    stats_line = f"{line[0]}: {line[1]} ({line[2]})"
    poll_results.append(stats_line)

poll_results.append(separator)
poll_results.append(winner_line)
poll_results.append(separator)

#write output file in Analysis folder
cleaned_file = zip(poll_results)
output_file = os.path.join("Analysis","output.txt")
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerows(cleaned_file)

#print results to terminal
for row in poll_results:
    print(row)
