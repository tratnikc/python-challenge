#open election data file
#get total number of votes cast
#list of candidates who received votes

import os
import csv

election_results = []
candidates = []
candidate_votes = {}
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
        candidate_votes = {"name" : running_man,
                            "vote_pct" : vote_pct,
                            "vote_count" : vote_count}
        tally_results.append(candidate_votes)

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
sorted_results = sorted(tally_results, key=lambda item:item['vote_count'], reverse=True)

header = "Election Results"
separator = "--------------------------"
total_line = f"Total Votes: {total_votes}"
winner_line = f"Winner: {sorted_results[0]['name']}"

poll_results.append(header)
poll_results.append(separator)
poll_results.append(total_line)
poll_results.append(separator)

for line in sorted_results:
    stats_line = f"{line['name']}: {line['vote_pct']} ({line['vote_count']})"
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
