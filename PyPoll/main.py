import os
import csv

election = {}

total_votes = 0
candidate = ""
votes_percent = 0

election_csv = os.path.join('Resources', 'election_data.csv')
        
with open (election_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    print("Election Results")
    print("_______________________")

    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        total_votes = total_votes + 1

        if candidate in election:
            election[candidate] = election[candidate] + 1
        else:
            election[candidate] = 1 

print(f"Total Votes: {total_votes}")
print("_______________________")

for key, value in election.items():
    print (key + ":" + str(value))
    
    

        
        
        
# The total number of votes cast



# A complete list of candidates who received votes


# The percentage of votes each candidate won


# The total number of votes each candidate won


# The winner of the election based on popular vote.