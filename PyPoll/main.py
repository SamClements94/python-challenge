import os
import csv

election_csv = os.path.join('Resources', 'election_data.csv')

election = {}

with open (election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        if row[2] in election:
            election[candidate] = election[candidate] + 1
        else:
            election[candidate] = 1
        print(election)
        
        
# The total number of votes cast
print("Election Results")
print("_______________________")

# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.