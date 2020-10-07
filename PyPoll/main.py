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

candidates = set(election_results)
total_votes = len(election_results)
tally_votes()

sorted_results = sorted(tally_results, key=lambda item:item['vote_count'], reverse=True)

print(sorted_results[0]["name"])

header = "Election Results"
separator = "-----------------------"
total_line = f"Total Votes: {total_votes}"
for line in sorted_results:
    print(line["name"])



"""
khan_votes = election_results.count("Khan")
correy_votes = election_results.count("Correy")
li_votes = election_results.count("Li")
otooley_votes = election_results.count("O'Tooley")


print(f"Total Votes: {total_votes}")
print(f"Khan: {khan_votes}")
print(f"Correy: {correy_votes}")
print(f"Li: {li_votes}")
print(f"O'Tooley: {otooley_votes}")
"""    


