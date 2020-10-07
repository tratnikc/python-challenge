#open election data file
#get total number of votes cast
#list of candidates who received votes

import os
import csv

election_results = []
candidates = []
candidate_votes = {}
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
        #print(f"{vote_pct}")
        candidate_votes.update({running_man : [vote_pct, vote_count]}) 
        #print(f"{running_man}: ({election_results.count(running_man)})")

# path to collect data from Resources folder
votes_csv = os.path.join("Resources", "election_data.csv")

with open(votes_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    for row in csvreader:
        election_results.append(row[2])
        #if candidates.count(row[2]) == 0:
        #    candidates.append(row[2])

candidates = set(election_results)
total_votes = len(election_results)

tally_votes()
print(candidate_votes)

print("---------------------")

khan_votes = election_results.count("Khan")
correy_votes = election_results.count("Correy")
li_votes = election_results.count("Li")
otooley_votes = election_results.count("O'Tooley")


print(f"Total Votes: {total_votes}")
print(f"Khan: {khan_votes}")
print(f"Correy: {correy_votes}")
print(f"Li: {li_votes}")
print(f"O'Tooley: {otooley_votes}")
    


